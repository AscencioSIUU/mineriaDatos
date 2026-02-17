# Análisis de Matrimonios en Guatemala (2009-2022)

## Requisitos Previos

- Python 3.8 o superior
- pip

## Instalación

1. Instala las dependencias:
```bash
pip install -r ../mineriaDatos/requirements.txt
```

## Pasos para Ejecutar el Proyecto

### Paso 1: Descarga de Datos
```bash
python web_scrapping.py
```
Este script descarga automáticamente los archivos de matrimonios del INE de Guatemala (2009-2022) y los guarda en la carpeta `data/`.

### Paso 2: Procesamiento de Datos
Abre y ejecuta el notebook:
```bash
jupyter notebook preprocessing.ipynb
```
O si prefieres Jupyter Lab:
```bash
jupyter lab preprocessing.ipynb
```

**¿Qué hace este notebook?**
- Consolida los 14 archivos anuales en un dataset unificado
- Limpia y estandariza los nombres de columnas
- Armoniza las categorías y etiquetas inconsistentes
- Convierte tipos de datos y maneja valores faltantes
- Genera el dataset final limpio

### Paso 3: Análisis y Clustering

Para el análisis completo, ejecuta los notebooks en el directorio padre:

```bash
cd ../mineriaDatos
jupyter notebook analysis.ipynb
jupyter notebook clustering.ipynb
```

**Orden recomendado:**
1. `analysis.ipynb` - Análisis exploratorio de datos
2. `clustering.ipynb` - Segmentación usando K-Means

## Archivos de Salida

- `data/` - Archivos descargados del INE
- Dataset procesado y limpio
- Gráficos y visualizaciones en `img/`

## Notas

- La descarga de datos puede tomar unos minutos
- El procesamiento completo puede tomar 5-10 minutos dependiendo de tu hardware
- Los archivos de datos ocupan aproximadamente 500MB