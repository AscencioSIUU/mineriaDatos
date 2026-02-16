import httpx
from selectolax.parser import HTMLParser
from pathlib import Path
import time

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Accept": "text/html, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "referrer": "https://www.ine.gob.gt/publicaciones3.php?c=82"
    }

BASE_URL = 'https://www.ine.gob.gt/bdatos_cargar.php'

DATASETS = ['Divorcios', 'Matrimonios']

OUTPUT_DIR = Path('data')

def get_links_for_year(client, year, periodo = 1):
    params = {
        'anio': year,
        'categoria': '82',
        'periodo': periodo,
        'dire': "https://www.ine.gob.gt/sistema/"
    }

    response = client.get(BASE_URL, params=params, headers=HEADERS)

    if response.status_code != 200:
        print(f'Failed to fetch, status {response.status_code}')
        return []
    
    tree = HTMLParser(response.text)
    print(tree)

    links = []
    for node in tree.css('a[href]'):
        span_child = node.css_first('span')

        if span_child and span_child.text(strip=True) in DATASETS:
            links.append((span_child.text(strip=True), node.attributes.get('href')))

    return links

def download_file(client, url, filepath):
    try:
        with client.stream("GET", url, headers=HEADERS) as response:
            response.raise_for_status()

            with open(filepath, 'wb') as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)

        print(f' Saved: {filepath.name}')
    except Exception as e:
        print(f' Error downloading: {url}: {e}')

def scrape():
    OUTPUT_DIR.mkdir(exist_ok=True)

    years_to_scrape = range(2009, 2023)

    with httpx.Client(timeout=30.0) as client:
        for year in years_to_scrape:
            print(f'Processing year {year}')

            files_found = get_links_for_year(client, year)

            if not files_found:
                print('Not matching datasets found')
                continue

            for dataset_name, url in files_found:
                extension = url.split('.')[-1]
                filename = f'{year}_{dataset_name}.{extension}'
                save_path = OUTPUT_DIR / filename

                print(f' Downloading {dataset_name}')
                download_file(client, url, save_path)

                time.sleep(6)


scrape()

