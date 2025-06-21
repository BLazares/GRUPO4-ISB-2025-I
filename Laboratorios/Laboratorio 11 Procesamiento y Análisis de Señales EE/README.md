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

- **Dispositivo**: Ultracortex Mark IV  
- **Electrodos utilizados**: 8 canales  
- **Frecuencia de muestreo**: 250 Hz  
- **Software de adquisición**: OpenBCI GUI / BrainFlow  
- *O también puedes usar* **[EEGBCI](https://www.physionet.org/content/eegmmidb/1.0.0/)**

> _Insertar imagen de configuración del headset o layout de electrodos_

---

## 2. Preprocesamiento

- **Filtro pasa banda aplicado**: 1–40 Hz  
- **Filtro notch**: 50 Hz para remover ruido eléctrico  
- **Eliminación de artefactos**: ICA (parpadeos, EMG)  
- **Interpolación de canales malos**  

> _Insertar imagen de señal cruda vs filtrada_  
> _Insertar imagen de componentes ICA_

---

## 3. Extracción de Características

- **Bandas de frecuencia**: Delta, Theta, Alpha, Beta, Gamma  
- **Análisis de espectro de potencia**: Método de Welch  
- **Transformada Wavelet discreta (DWT)**: Daubechies (db4), nivel 5  

> _Insertar gráficas de espectro por canal o topomapas por banda_

---

## 4. Optimización y Selección de Features

- **Normalización**: z-score  
- **Reducción de dimensionalidad**: PCA  
- **Selección de características relevantes**: energía, entropía, estadísticas por banda  

> _Insertar gráfico PCA o tabla de features seleccionadas_

---

## 5. Análisis Integrado con MNE Python

- **Módulos usados**: `Raw`, `Epochs`, `Evoked`, `ICA`, `montage`, `interpolate_bads`  
- **Visualización de eventos y épocas**  
- **Promedios evocados y mapas topográficos**  

> _Insertar imagen de épocas y eventos_  
> _Insertar topomapas_

---

## 6. Resultados y Visualizaciones

- **Comparación antes y después del preprocesamiento**  
- **Visualización por sujetos/clases**  
- **Distribución de características**  

> _Insertar gráficos resumen (boxplots, scatter PCA, matriz de correlación)_

---

## 7. Referencias

- MNE-Python: https://mne.tools/stable/index.html  
- EEGBCI Dataset: https://www.physionet.org/content/eegmmidb/1.0.0/  
- Tutorial oficial MNE: https://mne.tools/stable/auto_tutorials/intro/10_overview.html  
- GitHub ejemplos:
  - https://github.com/pareeknikhil/EEG
  - https://github.com/rohansrinivasan/brain-waves-emotions
  - https://github.com/AGhaderi/MNE-Preprocessing

---
