![Ushuaia_TIerra_Del_Fuego](https://github.com/edfedo/Practicas_Profesionalizantes_2_2024/blob/main/reports/figures/Front_b.jpg)

------------

![Ushuaia_TIerra_Del_Fuego](https://github.com/edfedo/Practicas_Profesionalizantes_2_2024/blob/main/reports/figures/Front_a.png)

<p align="left">
    <a href="https://bgh.com.ar/">
    <img src="https://img.shields.io/badge/copyright_photo-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="copyright photo" />
  </a>
</p>

[-] **Degree:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial.

[-] **Institution:** Politécnico Malvinas Argentinas  https://politecnico.tdf.gob.ar/

[-] **Subject:** Practicas Profesionalizantes 2 

[-] **Company for internships:** BGH https://bgh.com.ar/

[-] **Company Adress:** Islas Malvinas 2815, V9420 Río Grande, Tierra del Fuego - Argentina

[-] **Year:** 2024

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=edfedo" alt="Vistas de perfil" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
</p>

------------

[-] **cookiecutter.project:** Practicas Profesionalizantes 2 / Professional Practices 2

[-] **Developed by:** Team Practicas Profesionalizantes 2

| Name       | GitHub User      |
| ------------- | ------------- |
| Anabella Buccino | Abuccino |
| Alejandro Maclean | Alemac22 |
| Federido D'Oliveira | edfedo |
| Jonatan Suarez | JSuarez-Arg |


[-] **Project support:**

| Name       | Matter      |
| ------------- | ------------- |
| Nicolas Caballero | Practicas Profesionalizantes 2 |
| Martin Mirabete | Desarrollo de Sistema de IA |
| Federico Magaldi | Comunicación, Tecnología, Sociedad y Relaciones Laborales |
| Silvana Paez | Procesamiento del Habla |

[-] **Project video:**

- Por favor usar vlc para ver el video, o actualizar codecs en caso de no poder verlo o escuchar el sonido (Sigue el link y click View raw, esto descargara el video)

<p align="left">
    <a href="https://github.com/edfedo/Plazas_Disponibles_Hotelero/blob/main/references/Video_TP_V2_simplescreenrecorder-2024-07-18_00.21.25.mp4">
    <img src="https://img.shields.io/badge/Link_Project_Hotelero_Video-277D24?style=for-the-badge&logo=github&logoColor=white" alt="Project" />
  </a>
</p>

------------

[-] **cookiecutter.description:**

| Practicas Profesionalizantes 2 - Placas BGH |
| ------------- | 
| [-] Objetivo del Estudio
El propósito de este estudio es desarrollar un sistema automatizado basado en visión por computadora (Fotos) para detectar componentes faltantes en placas electrónicas de la empresa BGH. Utilizando un modelo YOLOv8, se busca optimizar los procesos de control de calidad y reducir los errores humanos en la inspección visual. Este enfoque mejora la eficiencia de la línea de producción al identificar de forma precisa y rápida los defectos en las placas. | 

------------

[-] **Dataset:** 

| BGH      |   
| ------------- |
| [-] El mismo fue obtenido de forma directa por medio de la empresa BGH |

Metodología

[-] 1. Preparación de los Datos
   
Se utilizó un conjunto de datos de imágenes de placas electrónicas proporcionado por BGH, que incluye imágenes anotadas con etiquetas para los componentes presentes en las placas. Los pasos clave fueron:

Montaje de Google Drive: El almacenamiento en Google Drive permitió acceder y procesar los datos directamente en la nube.

Organización del Dataset:

Las imágenes fueron separadas en carpetas para entrenamiento y validación.
Se utilizó la función train_test_split para dividir el conjunto de datos en un 90% para entrenamiento y un 10% para validación, asegurando una distribución representativa.
Gestión de Archivos Faltantes: Se implementó un control de errores para identificar y manejar casos donde las imágenes o etiquetas estuvieran ausentes, garantizando la calidad de los datos procesados.

[-] 2. Entrenamiento del Modelo

El modelo YOLOv8 (versión mediana, yolov8m.pt) fue entrenado utilizando los siguientes parámetros:

Tarea: Detección de objetos.

Número de Épocas: 50 épocas con un criterio de paciencia para detenerse si no se observan mejoras en 5 épocas consecutivas.

Resolución de Imágenes: 960 píxeles.

Tamaño del Lote: 16 imágenes.

Dataset: Configurado mediante un archivo YAML que especifica las rutas y clases del conjunto de datos.

[-] 3. Validación del Modelo

Posteriormente, se evaluó el modelo entrenado utilizando el conjunto de validación para medir su capacidad de detección en un entorno controlado.


[-] **Dataset Description:**

| BGH     |
| ------------- |
| [-] Resultados del Entrenamiento |

Resultados

El entrenamiento del modelo YOLOv8 produjo los siguientes resultados preliminares:

[-] Métricas de Entrenamiento:

El modelo mostró una convergencia estable, alcanzando valores óptimos en las métricas de pérdida (loss) para detección de objetos y clasificación.

[-] Validación:

El modelo logró identificar con alta precisión los componentes faltantes en las placas electrónicas.
Las métricas de desempeño (por ejemplo, precisión promedio - mAP) serán utilizadas para evaluar su eficacia.

El desarrollo de este modelo basado en YOLOv8 proporciona una solución eficiente para la detección de componentes faltantes en las placas electrónicas de BGH. Este enfoque tiene los siguientes beneficios:

Reducción de Errores Humanos: Mejora la consistencia y precisión en el proceso de inspección.

Optimización del Tiempo: Automatiza una tarea crítica en la línea de producción, aumentando la velocidad de detección.

Escalabilidad: El sistema puede adaptarse para detectar otros tipos de defectos o ser aplicado en productos similares.

Con base en estos resultados, el sistema representa un avance significativo en la calidad y eficiencia del proceso de producción de BGH, contribuyendo a su competitividad en el mercado. Pasos futuros incluyen el ajuste fino del modelo y la evaluación en escenarios reales para asegurar su implementación exitos

------------


[-] **Languages ​​and Tools**

<div id="header" align="left">
<img src="https://img.shields.io/badge/Cookiecutter-D4AA00?style=for-the-badge&logo=Cookiecutter&logoColor=white" />
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" />
</a>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
</a>
<img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white" />
</a>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</a>  
<img src="https://img.shields.io/badge/DataSet-05192D?style=for-the-badge&logo=datacamp&logoColor=65FF8F" />
</a> 
<img src="https://img.shields.io/badge/machine learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
</a>
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
</a> 
</div>

------------

<p align="left">
    <a href="https://github.com/alexandresanlim/Badges4-README.md-Profile#-contact-">
    <img src="https://img.shields.io/badge/Badges_4_README_Profile-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" alt="Badges 4 README Profile" />
  </a>
</p>

------------














<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Practicas_Profesionalizantes_2_2024

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         Practicas_Profesionalizantes_2_2024 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── Practicas_Profesionalizantes_2_2024   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes Practicas_Profesionalizantes_2_2024 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

