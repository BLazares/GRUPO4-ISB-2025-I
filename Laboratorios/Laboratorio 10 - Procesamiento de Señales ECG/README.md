## Actividad 4 - Separabilidad de señales EKG simuladas

### 🎯 Objetivo

Evaluar la separabilidad de señales EKG artificiales mediante la extracción de características, su representación en un espacio reducido de características (PCA) y la visualización de agrupamientos por clases.

---

### 🧪 Metodología

1. Se generaron **3 señales EKG base** simuladas usando `neurokit2`.
2. Se crearon **3 señales adicionales** modificando ligeramente las originales.
3. Se procesaron con `ecg_process()` y se extrajeron características.
4. Se almacenaron en un `DataFrame` con etiquetas por clase.
5. Se aplicó **PCA** para reducir a 2 dimensiones.
6. Se visualizaron los datos para identificar **separabilidad entre clases**.

---

### 📊 Tabla de características extraídas

<div align="center">

| Clase | Imagen de características extraídas |
|:-----:|:------------------------------------:|
| 0     | <img src="ruta/a/tabla_clase_0.png" width="70%" /> |
| 1     | <img src="ruta/a/tabla_clase_1.png" width="70%" /> |
| 2     | <img src="ruta/a/tabla_clase_2.png" width="70%" /> |

</div>

---

### 📉 Visualización 2D con PCA

<div align="center">

| Proyección PCA 2D | Descripción |
|:------------------:|:-----------:|
| <img src="ruta/a/proyeccion_pca.png" width="60%" /> | Distribución de las señales simuladas tras aplicar reducción de dimensionalidad (PCA) |

</div>

---

### ✅ Conclusión

- Si las clases están bien separadas en el espacio PCA, significa que las **características extraídas son suficientemente discriminantes**.
- Esta técnica puede servir para la **detección automática de patrones** en señales fisiológicas simuladas o reales, como el ECG.
- La simulación y análisis permiten ensayar técnicas de clasificación antes de aplicarlas a datos reales.

---

### 📁 Archivos Relacionados

| Archivo | Descripción |
|--------|-------------|
| `actividad_4_ekg.py` | Código fuente con generación y análisis de señales |
| `datos_ekg.csv` | Dataset generado con las características |
| Carpeta `imagenyvideos/` | Imágenes de resultados para presentar en el informe |

