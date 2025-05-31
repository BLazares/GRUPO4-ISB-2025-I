# 🧪 Laboratorio de EMG

## ✳️ Ejercicio A: Simulación de distintos grados de asimetría

---

### 🎯 Objetivo de la práctica

Estudiar cómo varía el *Symmetry Ratio* al alterar la amplitud relativa de la señal EMG del músculo izquierdo.  
El propósito es observar el impacto de diferentes niveles de desbalance muscular en la simetría, un aspecto fundamental en contextos clínicos como la rehabilitación neuromuscular.

---

### ⚙️ Metodología

<div align="center">

| 🧪 Parámetro              | 🔧 Valor         |
|--------------------------|------------------|
| Duración                 | `10 segundos`    |
| Frecuencia de muestreo   | `1000 Hz`        |
| Número de ráfagas        | `10 bursts`      |
| Nivel de ruido blanco    | `0.01`           |

</div>

   
2. A partir de esta señal, se generaron cinco pares de señales. El **Canal 1** se mantuvo constante (100 % de amplitud), mientras que el **Canal 2** se escaló al **20 %, 40 %, 60 %, 80 % y 100 %**.

---

### 💻 Código implementado

#### 📦 Instalación e importación de librerías

```python
# Solo si aún no se tiene instalado
!pip install neurokit2

# Importar librerías necesarias
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, integrate
```

---

#### 🧠 Simulación y creación de pares de señales

```python
# Parámetros de simulación
fs = 1000  # Frecuencia de muestreo (Hz)
duration = 10  # Duración en segundos
burst_number = 10
noise = 0.01
scales = [0.2, 0.4, 0.6, 0.8, 1.0]  # Escalas del canal 2

# Generar señal base
emg_base = nk.emg_simulate(duration=duration, burst_number=burst_number, noise=noise, sampling_rate=fs)

# Crear los pares de señales
pares = []
for factor in scales:
    canal1 = emg_base.copy()
    canal2 = canal1 * factor  # escalado del segundo canal
    pares.append((canal1, canal2))
```

---

### 📊 Visualización de los pares de señales

```python
plt.figure(figsize=(14, 10))
for i, (canal1, canal2) in enumerate(pares):
    plt.subplot(5, 1, i + 1)
    plt.plot(canal1, label="Canal 1 (100%)", alpha=0.8)
    plt.plot(canal2, label=f"Canal 2 ({int(scales[i]*100)}%)", alpha=0.8)
    plt.title(f"Par {i+1}: Escalado al {int(scales[i]*100)}%")
    plt.legend()
    plt.grid(True)
plt.tight_layout()
plt.show()
```

🖼️ **Ejemplo de señal EMG simulada y escalada**
<div align="center">

| Descripción                                | Imagen de referencia                           |
|--------------------------------------------|-------------------------------------------------|
| Ejemplo de señal EMG simulada y escalada   | [📷 Señales EMG](./Imágenes%20en%20el%20anexo/Senales_EMG.png) |
| Gráfico de comparación Symmetry Ratio      | [📊 Comparación](./Imágenes%20en%20el%20anexo/Comparacion.png) |
| 👉 FALTA insertar imagen canal escalado     | [🔗 Añadir aquí](./ruta/a/la/imagen_faltante.png) |
</div >
---

### 🧮 Cálculo del Symmetry Ratio

```python
symmetry_ratios = []

for factor in scales:
    # Canales
    canal1 = emg_base.copy()
    canal2 = emg_base * factor

    # Limpieza
    clean1 = nk.emg_clean(canal1, sampling_rate=fs)
    clean2 = nk.emg_clean(canal2, sampling_rate=fs)

    # Envolvente
    amp1 = nk.emg_amplitude(clean1)
    amp2 = nk.emg_amplitude(clean2)

    # Área bajo la curva (regla de Simpson)
    area1 = integrate.simpson(amp1, dx=1/fs)
    area2 = integrate.simpson(amp2, dx=1/fs)

    # Symmetry Ratio
    symmetry_ratio = area2 / area1 if area1 != 0 else np.nan
    symmetry_ratios.append(symmetry_ratio)

# Mostrar resultados
for i, ratio in enumerate(symmetry_ratios):
    print(f"Par {i+1} ({int(scales[i]*100)}%): Symmetry Ratio = {ratio:.3f}")
```

---

### 📉 Gráfico final: Symmetry Ratio vs % de escala

```python
plt.figure(figsize=(8, 5))
plt.bar([f"{int(s*100)}%" for s in scales], symmetry_ratios, color='skyblue', edgecolor='black')
plt.axhline(0.8, color='red', linestyle='--', label='Umbral clínico (80%)')
plt.title("Symmetry Ratio vs Porcentaje de Escala del Canal 2")
plt.xlabel("Porcentaje de Escala del Canal 2")
plt.ylabel("Symmetry Ratio")
plt.ylim(0, 1.1)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
```

🖼️ **Gráfico de comparación final**

### 🖼️ Imágenes de Resultados


<div align="center">

| 📌 Descripción                           | 📎 Imagen / Enlace de referencia                                |
|-----------------------------------------|------------------------------------------------------------------|
| 📷 Señal EMG simulada y escalada        | [Ver imagen](./Imágenes%20en%20el%20anexo/Senales_EMG.png)       |
| 📊 Gráfico de comparación final         | [Ver imagen](./Imágenes%20en%20el%20anexo/Comparacion.png)       |
| ⚠️ Falta insertar señal escalada canal 2| [🔗 Añadir imagen aquí](./ruta/a/imagen_faltante.png)            |

</div>

---

### 🧠 Reflexión

Se observa que el *Symmetry Ratio* disminuye proporcionalmente a medida que se reduce la amplitud del **Canal 2**.  
Cuando esta cae por debajo del **80 %**, también lo hace el ratio, lo cual sugiere un **umbral clínico relevante** para evaluar **asimetrías musculares** en fisioterapia o rehabilitación.  
Este análisis puede ser útil para detectar deficiencias neuromusculares o compensaciones motoras.

---

✅ **Conclusión**:  
Un *Symmetry Ratio* inferior al 80 % puede indicar un desbalance significativo en la actividad muscular bilateral, lo que debe ser considerado en procesos de evaluación clínica o diseño de terapias de rehabilitación.
