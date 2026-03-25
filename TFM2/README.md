# 🌍 Análisis global de felicidad y economía

## 1. Descripción del proyecto

Este proyecto explora la relación entre el desarrollo económico y el bienestar subjetivo a nivel mundial. Utilizando datos reales del World Happiness Report (2005-2022) y del Banco Mundial (PIB), se ha realizado un análisis completo que incluye:

- Limpieza y transformación de datos con Python (pandas).
- Análisis estadístico y exploratorio.
- Creación de un dashboard interactivo en Power BI.

El objetivo es responder preguntas como: ¿los países más ricos son también los más felices?, ¿cómo ha evolucionado la felicidad en los últimos años?, y ¿qué países destacan en ambos rankings?

## 2. Estructura del proyecto
TFM2/
├── data/
│ ├── raw/ # Datos originales (CSV)
│ │ ├── World_Happiness_2005_2022.csv
│ │ └── economia.csv
│ └── processed/ # Dataset final limpio
│ └── dataset_final.csv
├── notebooks/ # Scripts de Python
│ ├── 01_cargar_y_limpiar.py
│ └── 02_analisis_exploratorio.py
├── dashboard/ # Archivo de Power BI
│ └── dashboard_felicidad.pbix
├── outputs/ # Gráficos generados
│ └── evolucion_felicidad.png
├── docs/ # documentos escritos
└ └── informe_TFM.pdf # Informe explicativo
    └── README.me 


## 3. Herramientas utilizadas
- Python 3.8+ con pandas y matplotlib para el procesamiento y análisis.
- Power BI Desktop para el dashboard interactivo.

## 4. Resultados y conclusiones
Los principales hallazgos del análisis son:

Correlación débil entre PIB y felicidad (r = 0.177). El crecimiento económico no es el principal determinante del bienestar; factores como el apoyo social, la libertad o la percepción de corrupción tienen mayor peso.

Países nórdicos lideran la felicidad: Dinamarca (7.67), Finlandia (7.62), Noruega (7.48), Suiza (7.47), Islandia (7.46), Países Bajos (7.45), Suecia (7.38), Canadá (7.32), Nueva Zelanda (7.28) e Israel (7.27).

Grandes economías no son las más felices: China, Japón, Alemania, Francia e India tienen PIB elevado pero no aparecen en el top de felicidad.

Evolución temporal: la felicidad mundial aumentó en 2020 (5.76), coincidiendo con la pandemia de COVID-19, posiblemente por un mayor sentido de comunidad y apoyo social.

El dashboard interactivo permite explorar estos resultados visualmente mediante mapas, gráficos de dispersión, rankings y series temporales.

## 5. Próximos pasos
Como posibles ampliaciones del proyecto se plantean:

Incluir más indicadores económicos y sociales (desempleo, desigualdad, inflación, nivel educativo).

Aplicar modelos de regresión para cuantificar el impacto de cada variable en la felicidad.

Extender el análisis con datos de años más recientes (2023 y 2024).

## 6. Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue en el repositorio.

## 7. Autores y agradecimientos
Autora: Alba Vila Torra
Este proyecto ha sido desarrollado como Trabajo Final de Máster en Análisis de Datos.

Agradecimientos al equipo docente por la guía y a las fuentes de datos (World Happiness Report, Banco Mundial) por proporcionar información de calidad.

📌 Nota: El informe detallado con todo el análisis se encuentra en informe.pdf.

