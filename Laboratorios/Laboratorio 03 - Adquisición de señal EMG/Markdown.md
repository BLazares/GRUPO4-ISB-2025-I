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

<p align="center"><i>Figura 1: Posición de los electrodos según el protocolo seguido en el paper [4].</i></p>
<p align="center"><img src="Imágenes/los 3 tipos.jpg" width="400"></p>
<p align="center"><i>Figura 2: Posición de los electrodos según el protocolo seguido en el paper [4].</i></p>

#### <blockquote> Prueba 01: Deltoides

<p align="center"><img src="Anexos/IMG_tricep.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 3: MODIIIIIIIIIFICARRRRRRRLa medición del EMG del tríceps se realizó con el participante de pie, manteniendo el brazo relajado al costado del cuerpo. Se colocaron electrodos de superficie en la región del tríceps para captar la actividad eléctrica del músculo durante la contracción y el reposo.
</i></p>

<p align="center">
   
|  **Actividad Muscular - Tríceps en reposo** | **Actividad Muscular - Tríceps ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|
|<video src="https://github.com/user-attachments/assets/b501a6a4-6002-4526-81b7-ce0dc513d36a"></video>|<video src="https://github.com/user-attachments/assets/8ff2246f-7f49-48b0-aa0b-53cf2bd35a6a">|
<p align="center"><i>Tabla 2. Videos de adquisición de la señal EMG según dos tomas: en reposo y con el músculo ejerciendo fuerza. </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo y ejerciendo fuerza**|<image src="Anexos/S_triceps.png">|
<p align="center"><i>Tabla 3. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

### 2. Actividad muscular del gastrocnemio según la literatura:
<p align="justify"> En el estudio de Wang et al. (2021), se centra en la medición de la actividad EMG del gastrocnemio durante varias inclinaciones y tipos de marcha (caminar en plano, cuesta arriba, cuesta abajo, y subir/bajar escaleras). Se observa que la actividad EMG del gastrocnemio aumenta progresivamente al caminar cuesta arriba, sugiriendo una mayor activación muscular debido a la mayor demanda de fuerza en comparación con caminar en plano o cuesta abajo. Es importante medir la actividad EMG en estas diferentes condiciones para entender cómo varía la activación muscular y cómo optimizar los movimientos en la rehabilitación o el entrenamiento [5]. </p>

<p align="center"><img src="Anexos/Gastrocnemio paper.png" width="400"></p>

<p align="center"><i>Figura 4: Posición de los electrodos según el protocolo seguido en el paper [5].</i></p>

### 2.1. Diferencias metodológicas:
<p align="justify"> Es importante mencionar que, para esta prueba, buscamos simplificar el análisis de la activación muscular del gastrocnemio imitando la marcha con un solo movimiento: la elevación de pantorrillas. A diferencia del estudio mencionado, nuestro enfoque se centró en capturar la actividad eléctrica del músculo gastrocnemio mediante la flexión plantar, utilizando una elevación controlada. Esta metodología nos permitió medir de manera eficiente la actividad muscular en un entorno controlado, manteniendo el tobillo en una posición neutral y relajada, con los electrodos colocados en la cabeza lateral del gastrocnemio para captar los datos durante el movimiento.</p>
<a name="P2"></a>

#### <blockquote> Prueba 02: BICEPS BRAQUIAL

<p align="center"><img src="Anexos/IMG_pierna.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 5. La medición del EMG del gastrocnemio se realizó con el participante de pie, manteniendo el tobillo en una posición neutral y relajada. Se colocaron electrodos de superficie en la cabeza lateral del gastrocnemio para captar la actividad eléctrica del músculo durante la flexión plantar.</i></p>

<p align="center">
   
|  **Actividad muscular - Biceps Braquial** | **Actividad Muscular - Gastrocnemio en movimiento (flexión plantar)** | **Actividad Muscular - Gastrocnemio ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
|<video src="https://github.com/user-attachments/assets/69bd1254-6af8-402e-9ef5-aaed76e18859"></video>|<video src="https://github.com/user-attachments/assets/1bd88350-0676-4097-b603-db53ae502012"></video>|<video src="https://github.com/user-attachments/assets/b8c96a19-02b9-4811-9cc9-4b1174248aca"> | 
<p align="center"><i>
Tabla 4. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo, en movimiento y ejerciendo fuerza**|<image src="Anexos/S_gastro.png">|
<p align="center"><i>Tabla 5. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

<a name="P3"></a>

## **Discusión:**<a id="Discusión"></a>
<p align="justify">Para este laboratorio, se utilizó el sistema BITalino para la adquisición de señales EMG, capturando y analizando la actividad en distintos grupos musculares bajo diversas condiciones. La EMG de superficie ofrece una técnica no invasiva para medir la actividad eléctrica muscular, proporcionando información valiosa sobre la fisiología y función de los músculos. Al realizar las pruebas en cada músculo, se observó una variabilidad significativa en las características de activación y las respuestas, lo que demuestra que cada músculo tiene un comportamiento único frente a diferentes condiciones de esfuerzo. Además, cada señal obtenida fue graficada mediante un código en Python, permitiendo visualizar la señal a lo largo del tiempo y asi poder ver los distintos músculos. Estos resultados destacan la importancia de un análisis individual para comprender mejor la función de cada musculo.</p>


## **Referencias** <a name="id9"></a>


---

1. Cleveland Clinic. EMG (Electromyography): What It Is, Purpose, Procedure & Results [Internet]. Cleveland Clinic; [citado 12 abr 2025]. Disponible en: https://my.clevelandclinic.org/health/diagnostics/4825-emg-electromyography
2. Johns Hopkins Medicine. Electromyography (EMG) [Internet]. Johns Hopkins Medicine; [citado 12 abr 2025]. Disponible en: https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/electromyography-emg
3. Guzmán-Muñoz E, Méndez-Rebolledo G. Electromiografía en las Ciencias de la Rehabilitación. *Rev Salud Uninorte* [Internet]. 2018 [citado 12 abr 2025];34(3):753–765. Disponible en: https://www.redalyc.org/journal/817/81759607022/html/
4. Roldán EJ. Actividad electromiográfica del músculo deltoides en jugadores de rugby amateur durante el gesto técnico del placaje [Internet]. CONICET; 2017 [citado 12 abr 2025]. Disponible en: https://ri.conicet.gov.ar/bitstream/handle/11336/57638/CONICET_Digital_Nro.fc60ec59-4154-4aa8-91b4-e8fcf4184a4e_A.pdf
5. Khodadadi V, Nowshiravan Rahatabad F, Sheikhani A, Jafarnia Dabanloo N. A dataset of a stimulated biceps muscle of electromyogram signal by using Rossler chaotic equation. *Data Brief*. 2023;49:109438. doi:10.1016/j.dib.2023.109438
6. Domínguez Jiménez JA. Análisis de las señales EMG de superficie del bíceps durante la ejecución de ejercicios con pesas [Internet]. Cartagena: Universidad Tecnológica de Bolívar; 2015 [citado 12 abr 2025]. Disponible en: https://biblioteca.utb.edu.co/notas/tesis/0069071.pdf
7. Proença M, Mrotzeck K. BITalino (r)evolution Lab Guide: Home Guide 1 – EMG [Internet]. Lisbon: PLUX – Wireless Biosignals, S.A.; 2021 [citado 12 abr 2025]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf
8. biosignalsplux. Manual del usuario del sensor de electromiografía (EMG) [Internet]. 2021 [citado 12 abr 2025]. Disponible en: https://manuals.plus/es/biose%C3%B1ales/manual-del-sensor-de-electromiograf%C3%ADa-emg#axzz7y3EF2MKZ
