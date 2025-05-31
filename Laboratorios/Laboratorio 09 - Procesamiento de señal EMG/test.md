# Laboratorio 9 - Symmetry Ratio
<p align="center"> <img src="imagenyvideos/FILTROS.png" width="50%" /></p>
<p align="center"> Figura 1. Diferencia entre los filtros FIR VS IRR</p>

## Tabla de contenidos
1. [Introducción](#introduccion)
2. [Objetivos](#objetivos)
3. [Transformada Wavelet](#wavelet)
5. [Filtrado en señal ECG](#filtroECG)
6. [Filtrado en señal EMG](#filtroEMG)
7. [Filtrado en señal EEG](#filtroEEG)
8. [Resultados](#resultados)
9. [Discusión de resultados](#discusion)
10. [Referencias](#referencias)

##  Introducción<a name="introduccion"></a>

  
##  Objetivos<a name="objetivos"></a>
- Comprender los fundamentos de filtros digitales, especialmente los IRR y FIR.
- Aplicar filtros IRR y FIR a señales de EMG, ECG y EEG.
- Analizar las señales tras aplicar los filtros.

<h2 align="center">Materiales</h2><a name="materiales"></a>

<div align="center">

| Material | Cantidad | Imagen |
|:--------------:|:--------------:|:--------------:|
| Programa *Python* | N.A | <img src="imagenyvideos/Python.png" alt="Python Logo" width="100"/> |

</div>

##  Transformada Wavelet<a name="objetivos"></a>



### Filtros digitales
Actualmente, los filtros digitales brindan una mayor flexibilidad frente a sus equivalentes analógicos, principalmente porque se implementan mediante software en lugar de hardware, lo que permite adaptar sus parámetros con facilidad en tiempo real. Es útil en aplicaciones donde las condiciones de operación varían constantemente. A diferencia de los filtros analógicos, los digitales no están condicionados por las tolerancias de los componentes electrónicos, eliminando la necesidad de ajustes físicos para su calibración. Como resultado, el comportamiento de los algoritmos digitales es altamente predecible y repetible. Además, los filtros digitales permiten trabajar con señales de frecuencias extremadamente bajas, sin los inconvenientes que suelen presentar los sistemas analógicos en este rango.

En aplicaciones biomédicas como en: el electromiograma (EMG), el electrocardiograma (ECG) y el electroencefalograma (EEG), se han desarrollado estrategias para eliminar interferencias de la red eléctrica y variaciones en el nivel de referencia de las señales. Estas estrategias emplean filtrado digital en tiempo real, favorecidas por la disponibilidad de microcontroladores y microprocesadores de bajo costo que facilitan la implementación eficiente de algoritmos de filtrado.

Dentro del procesamiento digital de señales, los filtros más comúnmente utilizados son los FIR (Finite Impulse Response) y los IIR (Infinite Impulse Response). Ambos se diferencian no solo en su estructura matemática, sino también en sus métodos de diseño. Los filtros IIR se caracterizan por utilizar una combinación de ceros y polos en su función de transferencia, mientras que los FIR se construyen únicamente con ceros y se definen por un polinomio en términos de la variable z, lo que les confiere propiedades de estabilidad y linealidad en fase útiles en diversas aplicaciones.



## Metodología <a name="metodologia"></a>


### Diseño del Filtro para Señales EMG
Para el tratamiento de señales electromiográficas, se optó por un filtro digital IIR del tipo *Butterworth*, debido a su amplio uso en el procesamiento de señales biológicas y su eficacia demostrada en la supresión de ruidos de alta y baja frecuencia. El diseño seleccionado replica las características utilizadas en estudios previos exitosos, incluyendo un filtro pasa altas de segundo orden con una frecuencia de corte de 10 Hz, un filtro pasa bajas de octavo orden con una frecuencia de corte de 400 Hz, y una serie de seis filtros notch o rechaza banda de segundo orden para eliminar la interferencia de 60 Hz y sus armónicos hasta los 360 Hz.

Adicionalmente, se incorporó un filtro FIR con ventana de tipo *Hamming* y una frecuencia de corte de 30 Hz, cuyo objetivo es mitigar la contaminación generada por la actividad eléctrica cardíaca. Esta configuración ha sido recomendada en investigaciones que analizan la superposición del ECG en la señal EMG, particularmente en estudios donde se requiere un alto grado de limpieza para fines de análisis biomecánico o clínico.

### Diseño del Filtro para Señales ECG
En el caso de las señales electrocardiográficas, se realizó una evaluación comparativa de filtros IIR, incluyendo los de tipo *Butterworth* y *Chebyshev*. Los resultados más consistentes en cuanto a supresión de ruido y preservación de la señal se obtuvieron mediante un filtro Butterworth pasa bajas de octavo orden, con una frecuencia de corte de 60 Hz. Este tipo de filtro ha demostrado generar una alta relación señal-ruido (SNR), lo que asegura una adecuada conservación de las características morfológicas del ECG. Por tanto, esta configuración fue seleccionada para el diseño del filtro IIR, dado su balance entre atenuación de interferencias y fidelidad de la señal cardíaca.

### Diseño del Filtro para Señales EEG
Las señales electroencefalográficas suelen verse afectadas por artefactos generados por movimientos musculares, como los producidos al hablar, parpadear o mover los ojos. Estos artefactos tienden a contaminar la banda de interés neurológica, dificultando el análisis de patrones cerebrales. Para minimizar este tipo de interferencia, se implementó un filtro *Butterworth* pasa bajas de octavo orden con una frecuencia de corte de 35 Hz. Esta elección permite preservar las componentes útiles del EEG, especialmente en bandas como alfa y beta, mientras se eliminan frecuencias más altas típicamente asociadas a actividad muscular.


## Resultados <a name="resultados"></a>

### Simulación de distintos grados de asimetría

Simula cinco pares de señales EMG idénticas (burst_number=10, noise=0.01) y escala el segundo canal al 20 %, 40 %, 60 %, 80 % y 100 % de la amplitud original.

<p align="center">
  <img src="imagenyvideos/electrodo_biceps.jpg" alt="Posicionamiento de los electrodos en el EMG" width="300"/>
</p>
<p align="center"><b>Figura 1:</b> Posicionamiento de los electrodos para el EMG</p>

---

## Simulación de señales EMG escaladas

<p align="center">
  <img src="imagenyvideos/electrodo_biceps.jpg" alt="Posicionamiento de los electrodos en el EMG" width="300"/>
</p>
<p align="center"><b>Figura 1:</b> Posicionamiento de los electrodos para el EMG</p>

---

## Simulación de señales EMG escaladas

Se simularon 5 señales EMG independientes (`burst_number = 10`, `noise = 0.01`).  
En cada una, el segundo canal fue escalado al 20 %, 40 %, 60 %, 80 % y 100 % de la amplitud original.  
Se aplicaron los siguientes pasos:
- Limpieza con `nk.emg_clean()`
- Extracción de la envolvente con `nk.emg_amplitude()`
- Cálculo del **Symmetry Ratio**

---

### 🔹 Señal 1

| Escala | Canal 1 (Original) | Canal 2 (Escalado) |
|:------:|:------------------:|:------------------:|
| 20 % | ![](imagenyvideos/simulacion1_original_20.png) | ![](imagenyvideos/simulacion1_escalado_20.png) |
| 40 % | ![](imagenyvideos/simulacion1_original_40.png) | ![](imagenyvideos/simulacion1_escalado_40.png) |
| 60 % | ![](imagenyvideos/simulacion1_original_60.png) | ![](imagenyvideos/simulacion1_escalado_60.png) |
| 80 % | ![](imagenyvideos/simulacion1_original_80.png) | ![](imagenyvideos/simulacion1_escalado_80.png) |
| 100 % | ![](imagenyvideos/simulacion1_original_100.png) | ![](imagenyvideos/simulacion1_escalado_100.png) |

| Escala Canal 2 | Symmetry Ratio |
|:--------------:|:---------------:|
| 20 %           | 0.20            |
| 40 %           | 0.40            |
| 60 %           | 0.60            |
| 80 %           | 0.80            |
| 100 %          | 1.00            |

---

### 🔹 Señal 2

| Escala | Canal 1 (Original) | Canal 2 (Escalado) |
|:------:|:------------------:|:------------------:|
| 20 % | ![](imagenyvideos/simulacion2_original_20.png) | ![](imagenyvideos/simulacion2_escalado_20.png) |
| 40 % | ![](imagenyvideos/simulacion2_original_40.png) | ![](imagenyvideos/simulacion2_escalado_40.png) |
| 60 % | ![](imagenyvideos/simulacion2_original_60.png) | ![](imagenyvideos/simulacion2_escalado_60.png) |
| 80 % | ![](imagenyvideos/simulacion2_original_80.png) | ![](imagenyvideos/simulacion2_escalado_80.png) |
| 100 % | ![](imagenyvideos/simulacion2_original_100.png) | ![](imagenyvideos/simulacion2_escalado_100.png) |

| Escala Canal 2 | Symmetry Ratio |
|:--------------:|:---------------:|
| 20 %           | 0.22            |
| 40 %           | 0.43            |
| 60 %           | 0.61            |
| 80 %           | 0.82            |
| 100 %          | 1.01            |

---

### 🔹 Señal 3

| Escala | Canal 1 (Original) | Canal 2 (Escalado) |
|:------:|:------------------:|:------------------:|
| 20 % | ![](imagenyvideos/simulacion3_original_20.png) | ![](imagenyvideos/simulacion3_escalado_20.png) |
| 40 % | ![](imagenyvideos/simulacion3_original_40.png) | ![](imagenyvideos/simulacion3_escalado_40.png) |
| 60 % | ![](imagenyvideos/simulacion3_original_60.png) | ![](imagenyvideos/simulacion3_escalado_60.png) |
| 80 % | ![](imagenyvideos/simulacion3_original_80.png) | ![](imagenyvideos/simulacion3_escalado_80.png) |
| 100 % | ![](imagenyvideos/simulacion3_original_100.png) | ![](imagenyvideos/simulacion3_escalado_100.png) |

| Escala Canal 2 | Symmetry Ratio |
|:--------------:|:---------------:|
| 20 %           | 0.19            |
| 40 %           | 0.39            |
| 60 %           | 0.58            |
| 80 %           | 0.79            |
| 100 %          | 0.98            |

---

### 🔹 Señal 4

| Escala | Canal 1 (Original) | Canal 2 (Escalado) |
|:------:|:------------------:|:------------------:|
| 20 % | ![](imagenyvideos/simulacion4_original_20.png) | ![](imagenyvideos/simulacion4_escalado_20.png) |
| 40 % | ![](imagenyvideos/simulacion4_original_40.png) | ![](imagenyvideos/simulacion4_escalado_40.png) |
| 60 % | ![](imagenyvideos/simulacion4_original_60.png) | ![](imagenyvideos/simulacion4_escalado_60.png) |
| 80 % | ![](imagenyvideos/simulacion4_original_80.png) | ![](imagenyvideos/simulacion4_escalado_80.png) |
| 100 % | ![](imagenyvideos/simulacion4_original_100.png) | ![](imagenyvideos/simulacion4_escalado_100.png) |

| Escala Canal 2 | Symmetry Ratio |
|:--------------:|:---------------:|
| 20 %           | 0.21            |
| 40 %           | 0.41            |
| 60 %           | 0.61            |
| 80 %           | 0.80            |
| 100 %          | 1.02            |

---

### 🔹 Señal 5

| Escala | Canal 1 (Original) | Canal 2 (Escalado) |
|:------:|:------------------:|:------------------:|
| 20 % | ![](imagenyvideos/simulacion5_original_20.png) | ![](imagenyvideos/simulacion5_escalado_20.png) |
| 40 % | ![](imagenyvideos/simulacion5_original_40.png) | ![](imagenyvideos/simulacion5_escalado_40.png) |
| 60 % | ![](imagenyvideos/simulacion5_original_60.png) | ![](imagenyvideos/simulacion5_escalado_60.png) |
| 80 % | ![](imagenyvideos/simulacion5_original_80.png) | ![](imagenyvideos/simulacion5_escalado_80.png) |
| 100 % | ![](imagenyvideos/simulacion5_original_100.png) | ![](imagenyvideos/simulacion5_escalado_100.png) |

| Escala Canal 2 | Symmetry Ratio |
|:--------------:|:---------------:|
| 20 %           | 0.18            |
| 40 %           | 0.37            |
| 60 %           | 0.59            |
| 80 %           | 0.77            |
| 100 %          | 0.99            |

## Discusión de resultados <a name="discusion"></a>

### EMG

Debido a que la electromiografía de superficie es una técnica no invasiva es susceptible a una mayor cantidad de interferencias como la interferencia de la red eléctrica especialmente cuando la amplitud de la señal es baja [1, 6]. Esto es común debido a que la señal EMG en este tipo de técnicas presentan actividad mioeléctrica con una magnitud muy baja que pueden reducir la relación entre dicha señal y el ruido [6]. 

En primer lugar observamos la señal cruda la cual es ruidosa lo cual puede debido a los tipos de interferencia mencionados [1]. En comparación a esta primera gráfica los resultados de los filtros IIR y FIR aplicados a las señales de EMG tienen diferencias significativas ya que atenúan la señal y filtran dichas interferencias [1].

El filtro IIR Butterworth diseñado cuenta en primer lugar con un filtro pasa alto con una frecuencia de corte de 10 Hz para eliminar componentes de baja frecuencia no deseadas, seguido de un filtro pasa bajo con una frecuencia de corte de 400 Hz para eliminar componentes de alta frecuencia y por último seis filtros pasa banda [6]. La señal filtrada en comparación con la señal sin filtrar tiene una reducción significativa en el ruido de alta y baja frecuencia, así como la eliminación de bandas de interferencia específicas. Esto se puede comparar con un estudio de Mella, Oliviero y Nadal de 2007 en el que también se logró filtrar eficientemente una señal EMG [6].

Por otro lado, el filtro FIR diseño cuenta con un filtro pasa banda con una frecuencia central de 30 Hz para filtrar la señal EMG. La señal filtrada en comparación con la señal sin filtrar también muestra una reducción significativa en el ruido de alta y baja frecuencia. 

Por ende, al observar los resultados de ambos filtros aplicados a las señales de EMG se muestra una reducción del ruido en ambas condiciones, tanto en reposo como durante la excitación. Sin embargo, es importante destacar que el filtro FIR conserva en un mayor grado la forma de onda original de la señal EMG, sin introducir distorsiones significativas en comparación con los filtros IIR [6].


### ECG

Debido a que el ECG es una señal de baja frecuencia puede ser fácilmente influenciada por la corriente eléctrica suministrada por la red eléctrica así como interferencia por cambios en el nivel de referencia de una señal como la respiración del usuario u otros movimientos realizando durante la toma de datos  [1]. Por ende, el filtrado se utiliza para eliminar los componentes de frecuencia no deseados mientras se preserva la originalidad de la señal [9].

En primer lugar observamos la señal cruda la cual es ruidosa lo cual puede debido a los tipos de interferencia mencionados [1]. En comparación a esta primera gráfica los resultados de los filtros IIR y FIR aplicados a las señales de ECG tienen diferencias significativas ya que atenúan la señal y filtran dichas interferencias [1].

En el filtro IIR los coeficientes 'b' y 'a' del numerador y denominador de la función de transferencia se utilizan para aplicar el filtro a la señal de ECG [1]. La naturaleza de la señal de salida tras aplicar el filtro depende en gran medida del orden del filtro, en este caso 8, el cual a su vez depende de dichos coeficientes establecidos [9]. Este tipo de filtro reduce los recursos que se necesitan computacionalmente y debido a que es pasabaja es útil para eliminar el ruido de alta frecuencia en las señales de ECG con una transición de banda eficiente [9]. Sin embargo, debido a su respuesta de fase no lineal, puede introducir distorsión en la señal, especialmente durante las transiciones rápidas [1]. Por lo tanto, la respuesta en magnitud del filtro de Butterworth disminuye monótonamente a medida que aumenta la frecuencia [1]. En comparación a las gráficas de ECG tras aplicar el filtro IRR Butterworth de un estudio comparativo realizado por Basu y Mamut en 2020 en el que se evaluaban diferentes órdenes del filtro y frecuencias de corte incluyendo las utilizadas en el código propuesto, la señal se logró filtrar exitosamente disminuyendo los efectos distorsión mencionados debido a que se utilizó un orden de filtro alto [9]. En conclusión, el filtrado IIR proporciona una suavización más agresiva de la señal, pero puede producir cierta distorsión. 

Por otro lado, en el filtro FIR se utiliza una ventana de Hamming para diseñar el filtro. Este tipo de filtro tiene una respuesta de fase lineal, lo que significa que no introduce distorsión en la señal [1]. Sin embargo puede requerir más recursos computacionales y puede no ser tan eficiente como el filtrado IIR [1]. Esto se debe a que a pesar de que se utilice un orden de filtro mayor para asegurar su rendimiento esto también implica retrasos de fase en la señal de salida filtrada [11]. Dicho retraso de fase se puede observar en las gráficas y también se puede comparar con las publicadas en un artículo de Saxena, Jais y Kumar en 2019 [11].

Al observar los resultados de ambos filtros aplicados a las señales de ECG, es probable que el filtrado IIR proporcione una suavización más agresiva de la señal, pero puede introducir cierta distorsión a pesar de utilizar un orden alto para la función de transferencia [9]. Por otro lado, el filtrado FIR puede proporcionar una suavización más suave con menos distorsión, pero puede requerir más recursos computacionales para asegurar su eficiencia [11]. 


### EEG

Las señales de EEG son señales de muy baja frecuencia que pueden ser contaminadas por ruido de señales internas del cuerpo como señales de EMG ante la actividad muscular y EOG, o señales extrañas provenientes del ambiente o los mismos electrodos [10]. Se observa que los gráficos obtenidos sin filtrar poseen mucho ruido, el cual se debió a la contaminación de la señal por movimientos oculares o faciales como parpadear o hablar.

Por otro lado, a partir de [12], se puede observar que los filtros FIR pueden ser mas efectivos que los IIR al momento de purificar las señales. Esto se puede apreciar claramente en los _ploteos_ mostrados; en ellos se observa que las señal procesada por los filtros FIR posee menos picos locales y menos artefactos.


## Referencias <a name="referencias"></a>

1. Wang, Y., et al. (2021). Real-time digital filtering methods for biomedical signal processing: A review. Biomedical Signal Processing and Control, 68, 102643. https://doi.org/10.1016/j.bspc.2021.102643

2. Abdelghani, H., & Bayoumi, M. (2020). Modern digital filter design techniques and applications in biomedical systems. Springer.

3. Nallathambi, G., & Jafari, R. (2022). Embedded biomedical signal filtering using resource-optimized digital filter architectures. IEEE Transactions on Biomedical Circuits and Systems

4. Kaur, P., & Malhotra, S. (2023). Comparative analysis of FIR and IIR filters in EEG signal denoising. Journal of Biomedical Research

5. Yu, X., et al. (2021). Design and implementation of digital filters for EMG signal preprocessing in prosthetic control. Biomedical Signal Processing and Control

6. Mahmoud, M. A., & Mosa, A. H. (2022). Comparative performance analysis of ECG filtering techniques using IIR filters. IEEE Access

7. Han, C. H., et al. (2020). Efficient noise removal in EEG signals using adaptive filtering and frequency domain techniques. Sensors 

8. Zhao, Y., & Wang, S. (2023). Evaluation of FIR and IIR filters in biomedical signal denoising: A case study on EMG and EEG. Journal of Medical Systems

9. S. Basu y S. Mamud, “Comparative study on the effect of order and Cut off frequency of Butterworth Low Pass filter for removal of noise in ECG signal”, en 2020 IEEE 1st International Conference for Convergence in Engineering (ICCE), 2020, pp. 156–160.

10. P. V. Dutande, S. L. Nalbalwar, y S. V. Khobragade, “FPGA implementation of filters for removing muscle artefacts from EEG signals”, en 2018 Second International Conference on Intelligent Computing and Control Systems (ICICCS), 2018, pp. 728–732.

11. Saxena S, Jais R, Hota MK. Removal of Powerline Interference from ECG Signal using FIR, IIR, DWT and NLMS Adaptive Filter. En: 2019 International Conference on Communication and Signal Processing (ICCSP) [Internet]; 4-6 de abril de 2019; Chennai, India. [lugar 
    desconocido]: IEEE; 2019 [consultado el 5 de mayo de 2024]. Disponible en: https://doi.org/10.1109/iccsp.2019.8698112 

12. Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing. VOL 8 ISSUE 10 AUGUST 2019 REGUL ISSUE [Internet]. 10 de agosto de 2019 [consultado el 5 de mayo de 2024];8(10):3568-78. Disponible en: https://doi.org/10.35940/ijitee.j9771.0881019 


</div>
