# Procesamiento y Análisis de Señales EEG

## Introducción

La electroencefalografía (EEG) permite registrar la actividad eléctrica del cerebro mediante electrodos sobre el cuero cabelludo. Esta técnica es fundamental en investigación clínica, neurociencia y sistemas de interfaz cerebro-computadora. El procesamiento adecuado de estas señales es clave para eliminar artefactos, extraer características relevantes y entrenar modelos de aprendizaje automático.

Este proyecto utiliza señales EEG obtenidas con el headset Ultracortex Mark IV o bases públicas como EEGBCI/DEAP, procesadas con herramientas de Python, especialmente la biblioteca MNE.

## Objetivos

- Preprocesar señales EEG mediante filtrado y eliminación de artefactos.
- Extraer y optimizar características relevantes para tareas de clasificación.
- Usar MNE-Python para análisis temporal, frecuencial y espacial.

## Materiales

| Recurso                | Descripción                          |
|------------------------|--------------------------------------|
| Fuente de datos        | Ultracortex Mark IV / EEGBCI / DEAP  |
| Software               | Python, MNE, NumPy, SciPy, sklearn   |
| Frecuencia de muestreo | ~250 Hz                              |
| Número de electrodos   | 14–64 (según fuente)                 |

## Fase 1: Origen de los Datos

- **Ultracortex Mark IV**: adquisición propia (OpenBCI GUI).
- **EEGBCI**: tareas motoras imaginadas. [Enlace](https://www.physionet.org/content/eegmmidb/1.0.0/)
- **DEAP**: clasificación emocional. [Enlace](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/)

## Fase 2: Preprocesamiento

- **Filtros aplicados**: Notch (50/60 Hz), Pasa Banda (1–50 Hz).
- **Eliminación de artefactos**: ICA (parpadeo, EMG).
- **Normalización**: Z-score por canal.

## Fase 3: Extracción de Características

- **Tiempo**: RMS, MAV, Varianza.
- **Frecuencia**: Potencia por bandas (Delta, Theta, Alpha, Beta).
- **Tiempo-frecuencia**: Wavelet (db4).

## Fase 4: Optimización y Selección

- **Técnicas aplicadas**: PCA, normalización.
- **Transformaciones**: estadísticas y frecuencia.

## Referencias

1. Gorrell, D. (2020). *EEG con MNE-Python*. https://g0rella.github.io/gorella_mwn/preprocessing_eeg  
2. MNE-Python Docs. https://mne.tools/stable/auto_tutorials/intro/10_overview.html  
3. EEGBCI Dataset. https://www.physionet.org/content/eegmmidb/1.0.0/  
4. DEAP Dataset. https://www.eecs.qmul.ac.uk/mmv/datasets/deap/  
5. Ghaderi, A. (2021). *MNE Preprocessing*. https://github.com/AGhaderi/MNE-Preprocessing  
6. Pareek, N. (2020). https://github.com/pareeknikhil/EEG  
7. Srinivasan, R. (2020). https://github.com/rohansrinivasan/brain-waves-emotions  
