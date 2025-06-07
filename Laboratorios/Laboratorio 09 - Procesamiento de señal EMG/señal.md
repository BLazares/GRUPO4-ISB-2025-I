# 🧪 Actividad 4 - Separabilidad de señales EKG simuladas

## ✳️ Objetivo

Evaluar si señales EKG simuladas pueden agruparse en clases diferenciables tras extraer características, etiquetarlas y aplicar reducción de dimensionalidad.

---

## ⚙️ Metodología

<div align="center">

| Etapa                           | Descripción                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| 1️⃣ Señales originales          | Se simulan 3 señales EKG base                                              |
| 2️⃣ Señales simuladas           | Se generan 3 señales adicionales (variaciones de las originales)           |
| 3️⃣ Extracción de características | Análisis con `neurokit2`, valores extraídos y organizados en un DataFrame |
| 4️⃣ Reducción de dimensionalidad | Uso de PCA para proyección 2D y evaluación visual de separabilidad        |

</div>

---

## 1️⃣ Visualización de señales originales

<p align="center"><b>Señales EKG originales</b></p>

<div align="center">

| Señal original 0 | Señal original 1 | Señal original 2 |
|------------------|------------------|------------------|
| <img src="./imagenes_actividad4/original_0.png" width="90%"/> | <img src="./imagenes_actividad4/original_1.png" width="90%"/> | <img src="./imagenes_actividad4/original_2.png" width="90%"/> |

</div>

---

## 2️⃣ Visualización de señales simuladas

<p align="center"><b>Señales EKG adicionales (simuladas a partir de las originales)</b></p>

<div align="center">

| Señal simulada 0 | Señal simulada 1 | Señal simulada 2 |
|------------------|------------------|------------------|
| <img src="./imagenes_actividad4/simulada_0.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_1.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_2.png" width="90%"/> |

</div>

---

## 3️⃣ Características extraídas

<p align="center"><b>Resumen de características por clase (original y simuladas)</b></p>

<div align="center">

| Clase | Imagen con características |
|-------|-----------------------------|
| 0     | <img src="./imagenes_actividad4/caracteristicas_clase_0.png" width="80%"/> |
| 1     | <img src="./imagenes_actividad4/caracteristicas_clase_1.png" width="80%"/> |
| 2     | <img src="./imagenes_actividad4/caracteristicas_clase_2.png" width="80%"/> |

</div>

---

## 4️⃣ Visualización PCA - Reducción de dimensionalidad

<p align="center"><b>Distribución de señales EKG proyectadas en espacio 2D</b></p>

<div align="center">

| PCA Visualización |
|--------------------|
| <img src="./imagenes_actividad4/pca_resultado.png" width="60%"/> |

</div>

---

## 🧠 Interpretación

- Se observa cómo las señales originales y simuladas se agrupan (o no) en el espacio reducido.
- Si las clases están bien separadas, implica que las **características extraídas son útiles** para clasificación.
- El PCA permite evaluar de forma visual el nivel de **separabilidad de clases** en los datos simulados.

---

## ✅ Conclusión

El análisis de señales EKG simuladas y su visualización con PCA muestran si existe una estructura en los datos que permita distinguir entre clases.  
Esto es útil en contextos donde se desea entrenar clasificadores automáticos o evaluar patrones fisiológicos simulados.

---

## 📁 Archivos relacionados

| Archivo | Descripción |
|--------|-------------|
| `actividad4_separabilidad.md` | Informe en formato Markdown |
| `codigo_simulacion.py`       | Script para generación, análisis y visualización |
| `imagenes_actividad4/`       | Carpeta con imágenes del proyecto |

