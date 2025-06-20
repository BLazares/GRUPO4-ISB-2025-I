# Procesamiento y Análisis de Señales EEG con MNE-Python

## Introducción

La electroencefalografía (EEG) es una técnica no invasiva que registra la actividad eléctrica cerebral a través de electrodos colocados sobre el cuero cabelludo. Es ampliamente utilizada en neurociencia, diagnóstico clínico y sistemas de interfaz cerebro-computadora (BCI). El análisis de señales EEG implica una serie de pasos complejos debido a la baja relación señal-ruido, artefactos fisiológicos (como parpadeos y movimientos musculares), y variabilidad entre sujetos y sesiones.

Este proyecto tiene como objetivo desarrollar un pipeline de procesamiento para señales EEG obtenidas mediante el headset **Ultracortex Mark IV** o bases de datos públicas como **EEGBCI** o **DEAP**, utilizando herramientas del paquete **MNE-Python**. A partir del preprocesamiento, se extraerán características relevantes y se optimizarán para tareas de clasificación utilizando algoritmos de aprendizaje automático.

## Objetivos

- Realizar el preprocesamiento de señales EEG, incluyendo filtrado, corrección de artefactos y normalización.
- Extraer características estadísticas, espectrales y tiempo-frecuencia que representen la actividad cerebral.
- Aplicar técnicas de selección y transformación de características para mejorar el rendimiento de los modelos de clasificación.
- Integrar el análisis completo utilizando **MNE-Python** para visualización y validación.

## Materiales y Herramientas


| Elemento                   | Descripción                                     |
|----------------------------|-------------------------------------------------|
| Headset EEG                | Ultracortex Mark IV (opcional)                  |
| Base de datos              | EEGBCI / DEAP                                   |
| Software                   | Python, MNE, NumPy, SciPy, Scikit-learn, pandas |
| Frecuencia de muestreo EEG | ~250 Hz (según la fuente de datos)              |
| Número de electrodos       | 14–64 (según dispositivo o base de datos)       |

---

## Fase 1: Origen de los Datos

Dependiendo del enfoque experimental se utilizarán:

### a) Datos Propios con Ultracortex
- Headset: Ultracortex Mark IV
- Electrodos: 14
- Frecuencia de muestreo: 250 Hz
- Software de adquisición: OpenBCI GUI

### b) Base de Datos Pública
- EEGBCI Dataset  
  - URL: https://www.physionet.org/content/eegmmidb/1.0.0/  
  - Actividades: imaginaria de movimientos (MI)
- DEAP Dataset  
  - URL: https://www.eecs.qmul.ac.uk/mmv/datasets/deap/  
  - Actividades: estímulos audiovisuales y emociones

---

## Fase 2: Procedimiento de Preprocesamiento

- **Filtrado**:
  - Filtro Notch: 50/60 Hz para eliminar ruido de red.
  - Filtro Pasa Banda: 1–50 Hz para mantener frecuencias relevantes (delta, theta, alfa, beta).
- **Corrección de artefactos**:
  - Método: ICA (Análisis de Componentes Independientes).
  - Artefactos corregidos: parpadeo (EOG), interferencia muscular (EMG).
- **Normalización y alineación**:
  - Escalado Z-score por canal.
  - Sincronización temporal para alinear ensayos.

---

## Fase 3: Extracción de Características

Se extrajeron características del dominio del tiempo, frecuencia y tiempo-frecuencia:

### a) Dominio del Tiempo
- Media, Desviación estándar, Varianza
- MAV (Valor Absoluto Medio)
- RMS (Raíz Cuadrada Media)

### b) Dominio de la Frecuencia
- Potencia por bandas: Delta (1–4 Hz), Theta (4–8 Hz), Alpha (8–13 Hz), Beta (13–30 Hz)
- Análisis espectral usando la técnica de Welch

### c) Tiempo-Frecuencia
- Transformada Wavelet Discreta (DWT)
  - Wavelet: Daubechies (db4)
  - Niveles: 3–5

---

## Fase 4: Optimización y Selección de Características

- **Normalización**: estándar (Z-score), Min-Max
- **Reducción de dimensionalidad**:
  - PCA (Análisis de Componentes Principales)
  - Selección basada en importancia de características
- **Transformaciones estadísticas**:
  - Coherencia inter-canales
  - Entropía espectral
  - Fractal dimension

---

## Resultados Esperados
se colcoaran los resultados aquí


## Referencias

1. Gorrell, D. (2020). *Overview of MEG/EEG analysis with MNE Python*. Disponible en: https://g0rella.github.io/gorella_mwn/preprocessing_eeg  
2. MNE Developers. (2024). *MNE-Python documentation*. https://mne.tools/stable/auto_tutorials/intro/10_overview.html  
3. Goldberger AL, et al. (2000). *PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals*. Circulation.  
4. Koelstra, S., et al. (2012). *DEAP: A Database for Emotion Analysis using Physiological Signals*. IEEE Transactions on Affective Computing.  
5. Pareek, N. (2020). *EEG real-time acquisition and power spectrum analysis*. https://github.com/pareeknikhil/EEG  
6. Ghaderi, A. (2021). *MNE-Preprocessing*. https://github.com/AGhaderi/MNE-Preprocessing  
7. R. Srinivasan. (2020). *brain-waves-emotions: CNN for emotion classification from EEG*. https://github.com/rohansrinivasan/brain-waves-emotions

---
