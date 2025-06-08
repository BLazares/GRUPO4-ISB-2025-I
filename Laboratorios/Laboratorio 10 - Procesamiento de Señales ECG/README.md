# 🧪 Actividad 4 - Separabilidad de señales EKG simuladas

## ✳️ Objetivo

Evaluar la separabilidad entre señales EKG simuladas a partir de señales originales, extrayendo sus características, etiquetándolas por clase, y aplicando reducción de dimensionalidad (PCA).

---

## ⚙️ Metodología

<div align="center">

| Etapa | Descripción |
|-------|-------------|
| 1️⃣ Señales originales | Se simulan 3 señales EKG base (clases 0, 1, 2) |
| 2️⃣ Señales simuladas | Se generan 3 señales adicionales por cada original (total 9) |
| 3️⃣ Extracción de características | Se calcula un vector de atributos por señal |
| 4️⃣ Reducción de dimensionalidad | PCA en 2D para evaluar visualmente la separabilidad |

</div>

---

## 1️⃣ Visualización de señales originales

<p align="center"><b>Señales EKG originales</b></p>

<div align="center">

| Clase 0 | Clase 1 | Clase 2 |
|--------|---------|---------|
| <img src="./imagenes_actividad4/original_0.png" width="90%"/> | <img src="./imagenes_actividad4/original_1.png" width="90%"/> | <img src="./imagenes_actividad4/original_2.png" width="90%"/> |

</div>

---

## 2️⃣ Visualización de señales simuladas (3 por clase)

<p align="center"><b>Señales EKG simuladas (3 por clase)</b></p>

### 🔸 Simulaciones de Clase 0

<div align="center">

| Simulada 0.1 | Simulada 0.2 | Simulada 0.3 |
|-------------|--------------|--------------|
| <img src="./imagenes_actividad4/simulada_0_1.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_0_2.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_0_3.png" width="90%"/> |

</div>

### 🔹 Simulaciones de Clase 1

<div align="center">

| Simulada 1.1 | Simulada 1.2 | Simulada 1.3 |
|-------------|--------------|--------------|
| <img src="./imagenes_actividad4/simulada_1_1.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_1_2.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_1_3.png" width="90%"/> |

</div>

### 🔸 Simulaciones de Clase 2

<div align="center">

| Simulada 2.1 | Simulada 2.2 | Simulada 2.3 |
|-------------|--------------|--------------|
| <img src="./imagenes_actividad4/simulada_2_1.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_2_2.png" width="90%"/> | <img src="./imagenes_actividad4/simulada_2_3.png" width="90%"/> |

</div>

---

## 3️⃣ Características extraídas por clase

<p align="center"><b>Tabla resumen de atributos de cada clase</b></p>

<div align="center">

| Clase | Imagen de características |
|-------|----------------------------|
| 0     | <img src="./imagenes_actividad4/caracteristicas_clase_0.png" width="80%"/> |
| 1     | <img src="./imagenes_actividad4/caracteristicas_clase_1.png" width="80%"/> |
| 2     | <img src="./imagenes_actividad4/caracteristicas_clase_2.png" width="80%"/> |

</div>

---

## 4️⃣ Proyección PCA (Reducción a 2D)

<p align="center"><b>Visualización de la distribución de clases en 2D</b></p>

<div align="center">

| PCA Visualización |
|-------------------|
| <img src="./imagenes_actividad4/PCA.png" width="60%"/> |

</div>

---

## 🧠 Interpretación

- Cada grupo de señales simuladas mantiene relación con su señal original.
- Las características extraídas permitieron representar las señales en un espacio de menor dimensión.
- La visualización en 2D mediante PCA muestra la **separabilidad entre clases simuladas**.
- Esto sugiere que el método puede emplearse para clasificar señales de origen fisiológico con buena precisión si se entrenan modelos sobre estas características.

---

## ✅ Conclusión

Este ejercicio demuestra que señales EKG simuladas pueden ser diferenciadas entre clases al aplicar técnicas de extracción de características y reducción de dimensionalidad.  
Estas estrategias pueden utilizarse como base en aplicaciones de clasificación de señales biomédicas reales.

---

## 📁 Archivos relacionados

| Archivo | Descripción |
|--------|-------------|
| `actividad4_separabilidad.md` | Informe con estructura del experimento |
| `codigo_simulacion_clasificacion.py` | Script de generación y análisis |
| Carpeta `imagenes_actividad4/` | Contiene las gráficas y resultados exportados |
