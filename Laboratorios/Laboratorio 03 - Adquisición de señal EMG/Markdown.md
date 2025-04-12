# **Tabla de contenidos**

1. [Introducción](#id1)
2. [Propósito de la práctica](#id2)
3. [Materiales y equipos](#id3)\
     3.1 [Conexión usada](#id4)\
     3.2 [Mediciones en deltoides](#id5)\
     3.3 [Mediciones en bíceps](#id6)
5. [Resultados y limitaciones](#id7)\
     4.1 [Ploteo de la señal en OpenSignal](#id6)\
     4.2 [Archivos](#id7)\
     3.3 [Ploteo de la señal en Python](#id8)
7. [Referencias](#id9)



## **Introducción** <a name="id1"></a>
*La electromiografía (EMG) es una técnica para registrar señales eléctricas biomédicas obtenidas de la actividad neuromuscular (conjunto de interacciones entre el sistema nervioso y los músculos esqueleticos del cuerpo humano) [1] Las señales registradas pueden utilizarse en aplicaciones clínicas y biomédicas si se dispone de métodos avanzados de detección, descomposición, procesamiento y clasificación [2], pero las más comunes son monitorizar anomalías médicas y niveles de activación, así como para analizar la biomecánica [1].

El patrón de la señal EMG producida puede variar según la actividad muscular. *
*emg sirve para ..*
*emg funciona a partir de los principios...*


## **Propósito de la práctica** <a name="id2"></a>

* Adquirir señales biomédicas de EMG de músculos con menor indice de confusión técnica.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales EMG del software OpenSignals (r)evolution



## **Materiales y métodos** <a name="id3"></a>

<div align="center">

|       **Materiales**      | **Cantidad** |
|:-------------------------:|:------------:|
| (R)EVOLUTION Kit BITalino |       1      |
|           Laptop          |       1      |
|          Aplicación -     |       1      |
| Electrodos de superficie  |      5       |


</div>

*insertar imagenes de los materiales*
### **Conexión usada** <a name="id4"></a>
Se utilizó el EMG del bitalino
## **Resultados:**<a id="Resultados"></a>
<a name="P1"></a>
### 1. Actividad muscular del deltoides medial según la literatura:
<p align="justify">El deltoides medial es el principal responsable de la abducción del hombro en el plano frontal. Su actividad electromiográfica (EMG) es especialmente relevante en ejercicios como elevaciones laterales, levantamientos con carga y gestos deportivos que implican separación del brazo del tronco.

En el estudio de Roldán (2017), aunque se centra en el deltoides en general, se describe que durante el gesto técnico del placaje en rugby, la porción medial del deltoides presenta picos de activación significativos cuando el brazo se proyecta lateralmente. La actividad EMG se intensifica conforme aumenta la carga aplicada, con una frecuencia media (MF) que supera los 90 Hz en situaciones de esfuerzo máximo【4】.

Por su parte, Guzmán-Muñoz y Méndez-Rebolledo (2018) destacan que el deltoides medial muestra una respuesta electromiográfica muy clara y robusta ante ejercicios funcionales de tipo isométrico o isotónico, como la elevación del brazo en abducción. Se reporta una progresión en la amplitud RMS y en la frecuencia mediana (MDF) desde estados de reposo (~30–40 Hz) hasta esfuerzos elevados (~100–120 Hz)【3】.

La señal EMG en el deltoides medial es fácil de registrar por su localización superficial y su forma relativamente constante. La correcta colocación del electrodo, recomendada por las guías de Plux y BITalino, se realiza en la parte más prominente del músculo, a medio camino entre el acromion y la inserción deltoidea en el húmero, con los electrodos colocados paralelos a las fibras musculares【7】【8】.



<p align="center"><img src="Imágenes/biceps.jpg" width="400"></p>

<p align="center"><i>Figura 1. A) Ubicación de los electrodos de registro en el músculo deltoides, específicamente en sus porciones anterior (DA), medial (DM) y posterior (DP), siguiendo la disposición recomendada por el estudio de Roldán (2017), basada en protocolos SENIAM. B) Montaje experimental durante la ejecución de ejercicios de abducción con carga progresiva. C) Registro videográfico del gesto técnico en plano frontal para control postural y análisis cinemático complementario.</i></p>
<p align="center"><img src="Imágenes/los 3 tipos.jpg" width="800"></p>
<p align="center"><i>Figura 2. Representación de la señal EMG registrada en el deltoides medial durante el movimiento de abducción del brazo en tres condiciones: i) sin peso, ii) con carga mínima, y iii) con carga máxima. Se observa un incremento progresivo tanto en la amplitud como en la densidad espectral de la señal EMG, lo cual refleja un mayor reclutamiento de unidades motoras ante el aumento de la carga..</i></p>

<div align="center">


### 🏋️‍♂️ Datos fisiológicos del Deltoides Medial (basados en Roldán, 2017 y Guzmán-Muñoz & Méndez-Rebolledo, 2020)

| Condición muscular             | Frecuencia media (Hz) | Amplitud RMS estimada     |
|-------------------------------|------------------------|----------------------------|
| Reposo                        | ~30–40                 | Baja (~100–300 μV)*        |
| Abducción con carga moderada  | ~60–90                 | Media (~400–800 μV)*       |
| Abducción con carga elevada   | ~100–120               | Alta (~900–1500+ μV)*      |


#### <blockquote> Prueba 01: Deltoides

<p align="center"><img src="Anexos/IMG_tricep.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 3: MODIIIIIIIIIFICARRRRRRRLa medición del EMG del Deltoides se realizó con el participante de pie, manteniendo el brazo relajado al costado del cuerpo. Se colocaron electrodos de superficie en la región del Deltoides para captar la actividad eléctrica del músculo durante la contracción y el reposo.
</i></p>

<p align="center">
   
| **Actividad Muscular - Deltoides en reposo** | **Actividad Muscular - Deltoides ejerciendo fuerza (Toma 1)** | **Actividad Muscular - Deltoides ejerciendo fuerza (Toma 2)** |
|:-------------------------------------------:|:------------------------------------------------------------:|:------------------------------------------------------------:|
| <video src="https://github.com/user-attachments/assets/b501a6a4-6002-4526-81b7-ce0dc513d36a"></video> | <video src="https://github.com/user-attachments/assets/8ff2246f-7f49-48b0-aa0b-53cf2bd35a6a"></video> | <video src="https://github.com/user-attachments/assets/8ff2246f-7f49-48b0-aa0b-53cf2bd35a6a"></video> |

<p align="center"><i>Tabla 2. Videos de adquisición de la señal EMG del deltoides: reposo y dos tomas bajo contracción con carga.</i></p>


<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo y ejerciendo fuerza**|<image src="Anexos/S_triceps.png">|
<p align="center"><i>Tabla 3. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>



### 2. Actividad muscular del bíceps braquial según la literatura:
<p align="justify"> El bíceps braquial es un músculo biarticular que participa en movimientos de flexión del codo y supinación del antebrazo. Por su importancia funcional, ha sido ampliamente estudiado mediante electromiografía (EMG), permitiendo evaluar su actividad en condiciones de reposo, carga leve y carga máxima.

En el trabajo de Domínguez Jiménez (2015), se analiza la señal EMG del bíceps durante la ejecución de ejercicios con mancuernas, encontrando un incremento progresivo en la amplitud y frecuencia de la señal conforme aumenta la carga. El estudio reporta una frecuencia media (MF) que va desde los 30–60 Hz en contracción leve, hasta valores superiores a los 100 Hz en contracciones máximas, con una amplitud promedio que puede superar los 1500 μV bajo carga intensa【6】.

Por otro lado, el estudio de Khodadadi et al. (2023) explora el comportamiento del bíceps braquial bajo estimulación artificial utilizando la ecuación caótica de Rossler. En este caso, se genera una señal EMG con características no lineales y frecuencias superiores a 120 Hz, útiles para el análisis de patrones complejos en contextos como el desarrollo de prótesis inteligentes o clasificación de señales patológicas【5】.

Además, las guías clínicas de Cleveland Clinic y Johns Hopkins Medicine confirman que el análisis EMG del bíceps es fundamental para diagnosticar lesiones musculares, evaluar el rendimiento motor y personalizar la rehabilitación【1】【2】.

La colocación adecuada de los electrodos también es clave. Según Proença y Mrotzeck (2021), se recomienda ubicar los electrodos paralelos a las fibras musculares del bíceps, aproximadamente en el centro del vientre muscular, siguiendo lineamientos del proyecto SENIAM para garantizar registros fiables y comparables【7】.

Por último, Guzmán-Muñoz y Méndez-Rebolledo (2018) subrayan el uso de EMG en ciencias de la rehabilitación, considerando al bíceps braquial como músculo clave en la restauración de funciones básicas del miembro superior en pacientes con daño neuromuscular【3】.
<p align="center"><img src="Imágenes/biceps position.jpg" width="500"></p>
<p align="center"><i>Figura 6. Disposición anatómica de los electrodos para el registro electromiográfico del bíceps braquial. Los electrodos activos se colocan paralelos a las fibras musculares, centrados en el vientre del músculo, con una separación de aproximadamente 2 cm entre ellos, tal como lo establece el protocolo SENIAM. El electrodo de referencia (masa) se posiciona en una zona ósea neutra del antebrazo.</i></p>
<p align="center"><img src="Imágenes/biceps2.0.jpg" width="500"></p>
<p align="center"><i>Figura 7. Registro de la señal electromiográfica superficial del bíceps braquial durante una secuencia de contracción voluntaria, relajación y nueva contracción. Se evidencia un aumento significativo en la amplitud de la señal (hasta 0.125 V) durante las fases activas, con reducción casi total en los períodos de reposo, lo cual refleja un patrón de activación típico en ejercicios de flexión de codo bajo carga moderada.</i></p>

###   Datos fisiológicos del Bíceps Braquial (según literatura)
| Condición muscular           | Frecuencia media (Hz) | Amplitud media (μV)       |
|-----------------------------|------------------------|----------------------------|
| Descanso                    | ~20–40                 | Baja (~100–300 μV)         |
| Contracción leve            | ~30–60                 | ~200–500 μV                |
| Contracción fuerte          | ~60–110                | ~600–1500 μV               |

#### <blockquote> Prueba 02: Bíceps braquial / Nervio mediano

<p align="center"><img src="Anexos/IMG_mano.jpeg" width="450" height="300"></p>

<p align="center"><i>Figura 7: La medición del EMG del nervio mediano se realizó con el participante en una posición sentada, manteniendo una postura natural con los codos apoyados en los reposabrazos y la cabeza en una posición neutral para minimizar la interferencia de otros movimientos.</i></p>

<p align="center">
   
|  **Actividad Muscular - Bíceps braquial/nervio mediano en reposo** | **Actividad Muscular - Bíceps braquial/nervio mediano en movimiento** | **Actividad Muscular - Bíceps braquial/nervio mediano ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|  
| <video src="https://github.com/user-attachments/assets/e188c019-ad6a-4d4c-baf0-48036068a712"> | <video src="https://github.com/user-attachments/assets/750503ff-88bb-4193-a935-c3d0a1321b8b"> | <video src="https://github.com/user-attachments/assets/84ebebe4-5c92-4557-954f-179f88f1f5e8"> | 
<p align="center"><i>Tabla 6. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo, en movimiento y ejerciendo fuerza**|<image src="Anexos/S_mano.png">|  
<p align="center"><i>Tabla 7. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>


## **Discusión:**<a id="Discusión"></a>
<p align="justify">Para este laboratorio, se utilizó el sistema BITalino para la adquisición de señales EMG, capturando y analizando la actividad en distintos grupos musculares bajo diversas condiciones. La EMG de superficie ofrece una técnica no invasiva para medir la actividad eléctrica muscular, proporcionando información valiosa sobre la fisiología y función de los músculos. Al realizar las pruebas en cada músculo, se observó una variabilidad significativa en las características de activación y las respuestas, lo que demuestra que cada músculo tiene un comportamiento único frente a diferentes condiciones de esfuerzo. Además, cada señal obtenida fue graficada mediante un código en Python, permitiendo visualizar la señal a lo largo del tiempo y asi poder ver los distintos músculos. Estos resultados destacan la importancia de un análisis individual para comprender mejor la función de cada musculo.</p>

## **Referencias** <a id="*Referencias"></a>

1. Cleveland Clinic. EMG (Electromyography): What It Is, Purpose, Procedure & Results [Internet]. Cleveland Clinic; [citado 12 abr 2025]. Disponible en: https://my.clevelandclinic.org/health/diagnostics/4825-emg-electromyography

2. Johns Hopkins Medicine. Electromyography (EMG) [Internet]. Johns Hopkins Medicine; [citado 12 abr 2025]. Disponible en: https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/electromyography-emg

3. Guzmán-Muñoz E, Méndez-Rebolledo G. Electromiografía en las Ciencias de la Rehabilitación. *Rev Salud Uninorte* [Internet]. 2018 [citado 12 abr 2025];34(3):753–765. Disponible en: https://www.redalyc.org/journal/817/81759607022/html/

4. Roldán EJ. Actividad electromiográfica del músculo deltoides en jugadores de rugby amateur durante el gesto técnico del placaje [Internet]. CONICET; 2017 [citado 12 abr 2025]. Disponible en: https://ri.conicet.gov.ar/bitstream/handle/11336/57638/CONICET_Digital_Nro.fc60ec59-4154-4aa8-91b4-e8fcf4184a4e_A.pdf

5. Khodadadi V, Nowshiravan Rahatabad F, Sheikhani A, Jafarnia Dabanloo N. A dataset of a stimulated biceps muscle of electromyogram signal by using Rossler chaotic equation. *Data Brief*. 2023;49:109438. doi:10.1016/j.dib.2023.109438

6. Domínguez Jiménez JA. Análisis de las señales EMG de superficie del bíceps durante la ejecución de ejercicios con pesas [Internet]. Cartagena: Universidad Tecnológica de Bolívar; 2015 [citado 12 abr 2025]. Disponible en: https://biblioteca.utb.edu.co/notas/tesis/0069071.pdf

7. Proença M, Mrotzeck K. BITalino (r)evolution Lab Guide: Home Guide 1 – EMG [Internet]. Lisbon: PLUX – Wireless Biosignals, S.A.; 2021 [citado 12 abr 2025]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf

8. biosignalsplux. Manual del usuario del sensor de electromiografía (EMG) [Internet]. 2021 [citado 12 abr 2025]. Disponible en: https://manuals.plus/es/biose%C3%B1ales/manual-del-sensor-de-electromiograf%C3%ADa-emg#axzz7y3EF2MKZ

