# Laboratorio de actividad de procesamiento y análisis de señales EEG

## Contenidos
1. [Origen de los Datos](#1-origen-de-los-datos)
2. [Preprocesamiento](#2-preprocesamiento)
3. [Extracción de Características](#3-extracción-de-características)
4. [Optimización y Selección de Features](#4-optimizacion-y-seleccion-de-features)
5. [Análisis Integrado con MNE Python](#5-analisis-integrado-con-mne-python)
6. [Resultados y Visualizaciones](#6-resultados-y-visualizaciones)
7. [Referencias](#7-referencias)

---

## 1. Origen de los Datos

- **Fuente de datos**:  
  - Registros propios con headset **Ultracortex Mark IV**  
  - O base de datos pública como:  
    - **EEGBCI**: [https://www.physionet.org/content/eegmmidb/1.0.0/](https://www.physionet.org/content/eegmmidb/1.0.0/)
    - **DEAP**: [https://www.eecs.qmul.ac.uk/mmv/datasets/deap/](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/)

- **Especificaciones técnicas (Ultracortex)**:
  - Frecuencia de muestreo: 250 Hz
  - Número de electrodos: 8
  - Software de adquisición: OpenBCI GUI

> _Insertar imagen de configuración del headset o layout de electrodos_

---

## 2. Preprocesamiento

### Objetivo:
Limpiar las señales EEG mediante:
- Filtros: pasa banda, notch, wavelet
- Eliminación de artefactos: blink, EMG, ECG
- Normalización y alineación entre sesiones y sujetos

### Técnicas utilizadas:
- **Filtro pasa banda**: 1–40 Hz  
- **Filtro notch**: 50 Hz para eliminar interferencia de red  
- **ICA**: para remover artefactos fisiológicos  
- **Interpolación** de canales malos  

> _Insertar imagen de señal cruda vs filtrada_  
> _Insertar imagen de componentes ICA_

Referencias:
- [Tutorial MNE: Preprocesamiento EEG](https://g0rella.github.io/gorella_mwn/preprocessing_eeg)  
- [Documentación oficial MNE Python](https://mne.tools/stable/auto_tutorials/intro/10_overview.html)

---

## 3. Extracción de Características

### Detalles del análisis:
- **Análisis Wavelet**:  
  - Tipo: Daubechies (db4)  
  - Nivel: 5  
- **Bandas EEG**:
  - Delta (1–4 Hz)
  - Theta (4–8 Hz)
  - Alpha (8–13 Hz)
  - Beta (13–30 Hz)
  - Gamma (>30 Hz)
- **Técnicas**:
  - Espectro de potencia (Welch)
  - Estadísticas temporales y frecuenciales: media, energía, entropía

> _Insertar gráficas de espectro por canal o topomapas por banda_

---

## 4. Optimización y Selección de Features

### Objetivo:
Mejorar la calidad de los datos antes de alimentar modelos de clasificación.

### Técnicas:
- **Normalización**: z-score
- **Transformación**: PCA para reducción de dimensionalidad
- **Selección de características**: 
  - Energía por banda
  - Entropía
  - Coherencia
  - Estadísticas por canal

> _Insertar gráfico PCA o tabla de features seleccionadas_

### Ejemplos de referencia:
- [EEG real-time acquisition y análisis de coherencia](https://github.com/pareeknikhil/EEG/blob/master/UltraCortex/src/denoise.py)  
- [Clasificación de emociones con CNN y EEG](https://github.com/rohansrinivasan/brain-waves-emotions)

---

## 5. Análisis Integrado con MNE Python

### Objetivo:
Analizar datos en el dominio temporal, frecuencial y espacial con herramientas de MNE.

### Funcionalidades utilizadas:
- `Raw`, `Epochs`, `Evoked`
- `ICA`, `montage`, `interpolate_bads`

> _Insertar imagen de visualización de eventos y épocas_  
> _Insertar imagen de topomapas o actividad evocada_

Material recomendado:
- [Guía paso a paso con MNE](https://g0rella.github.io/gorella_mwn/preprocessing_eeg)
- [Repositorio AGhaderi - Preprocessing](https://github.com/AGhaderi/MNE-Preprocessing)

---

## 6. Resultados y Visualizaciones

- Comparación de señales antes y después del preprocesamiento  
- Mapas topográficos de actividad por banda  
- Gráficas de distribución de características  
- Visualización por clases o condiciones experimentales

> _Insertar resultados: gráficos, boxplots, mapas cerebrales, etc._

---

## 7. Referencias

- MNE-Python: https://mne.tools/stable/index.html  
- EEGBCI Dataset: https://www.physionet.org/content/eegmmidb/1.0.0/  
- DEAP Dataset: https://www.eecs.qmul.ac.uk/mmv/datasets/deap/  
- Tutorial MNE: https://g0rella.github.io/gorella_mwn/preprocessing_eeg  
- Ejemplos GitHub:
  - https://github.com/pareeknikhil/EEG
  - https://github.com/rohansrinivasan/brain-waves-emotions
  - https://github.com/AGhaderi/MNE-Preprocessing

---
