F# **LABORATORIO 5: – Uso de BiTalino para  Electroencefalograma (EEG)**



# **Laboratorio semana 6: Electroencefalograma**


# **Tabla de contenidos**
1. [Introducción al laboratorio](#id0)\
1.1 [¿Qué es EEG?](#id1)\
1.2 [Aplicaciones](#id2)\
1.3 [Tipos de medición de EEG](#id3)\
1.4 [¿De qué forma obtenemos la señal?](#id4)
2. [Objetivos](#id5)
3. [Materiales y equipos](#id6)
4. [Procedimiento](#id7)\
4.1 [Medición y Adquisición por electrodos](#id8)\
4.2 [Protocolo de adquisición](#id9)
5. [Resultados](#id10)\
5.1 [Fotos de conexión usada](#id11)\
5.2 [Señal con MarckOpenBCI4](#id12)\
    5.2.1 [Gráficas del OpenBCI](#id13)\
5.3 [Señal con Bitalino](#id14)\
    5.3.1 [Videos utilizando el Bitalino](#id15)\
    5.3.2 [Análisis de gráficas](#id16)
6. [Conclusiones](#id17)
7. [Referencias](#id18)

## **Introducción al laboratorio 5 EEG** <a name="id0"></a>

<p align="center"> 
  <img src="IMÁGENES Y VIDEOS/cefalograma.gif" width="50%" />
</p>



### ¿Qué es EEG? <a name="id1"></a>
<p align="justify">El electroencefalograma (EEG) es una herramienta fundamental en neurofisiología que permite registrar la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. Esta técnica no invasiva capta las oscilaciones eléctricas generadas por las neuronas corticales, reflejando distintos estados funcionales del cerebro.

Las señales EEG se clasifican en diferentes bandas de frecuencia, cada una asociada a funciones cognitivas y estados de conciencia específicos. A continuación, se describen estas bandas en orden descendente de frecuencia:

* Ondas Gamma (>30 Hz): Relacionadas con procesos cognitivos de alto nivel, como la percepción consciente, la integración sensorial y la memoria de trabajo.
* Ondas Beta (13–30 Hz): Asociadas con la atención activa, el pensamiento lógico y la resolución de problemas.
* Ondas Alfa (8–12 Hz): Presentes en estados de relajación y calma mental, especialmente con los ojos cerrados.
* Ondas Theta (4–7 Hz): Relacionadas con estados de somnolencia, meditación profunda y procesamiento emocional.
* Ondas Delta (0.5–4 Hz): Predominan durante el sueño profundo y están asociadas con procesos de reparación y regeneración.

El análisis de estas ondas proporciona información valiosa sobre el estado funcional del cerebro, permitiendo la identificación de patrones normales y anómalos. Por ejemplo, alteraciones en la actividad de las ondas gamma han sido observadas en trastornos como la esquizofrenia y el Alzheimer. </p>

<p align="center"> <img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%" /></p>
<p align="center"> Figura 1. Actividad cerebral.</p>
    



### Aplicaciones <a name="id2"></a>
---
<p align="justify"> El electroencefalograma (EEG) es una herramienta diagnóstica no invasiva que registra la actividad eléctrica cerebral a través de electrodos colocados en el cuero cabelludo. Su capacidad para detectar alteraciones en los patrones de ondas cerebrales lo convierte en un recurso valioso en diversas aplicaciones :

1. Diagnóstico de epilepsia y trastornos convulsivos
   El EEG es fundamental para identificar descargas epileptiformes y diferenciar entre tipos de crisis epilépticas, facilitando un tratamiento adecuado.

2. Evaluación de trastornos del sueño
   Integrado en estudios de sueño (polisomnografía), ayuda a diagnosticar condiciones como apnea del sueño, insomnio y narcolepsia.

3. Monitoreo en unidades de cuidados intensivos (UCI)
   Se utiliza para detectar convulsiones no evidentes clínicamente y evaluar el estado cerebral en pacientes comatosos o bajo anestesia.

4. Diagnóstico de encefalopatías y demencias
   Puede mostrar patrones anormales asociados con enfermedades como el Alzheimer o encefalopatías metabólicas e infecciosas.

5. Evaluación de lesiones cerebrales
   Tras un traumatismo craneoencefálico, el EEG permite estimar la extensión del daño y monitorear la recuperación neurológica.
.</p>
<p align="center"> <img src="IMÁGENES Y VIDEOS/imagen_2.jpg" width="60%" /></p>
<p align="center"> Figura 3. Aplicación clínica del EEG.</p>

### Tipos de medición de EEG <a name="id3"></a>
En el laboratorio utilizaremos el sistema **BITalino** para registrar la actividad eléctrica del cerebro (EEG). Dependiendo de cómo se coloquen los electrodos, existen tres tipos principales de medición:

* Monopolar:
  Se mide la diferencia de voltaje entre un electrodo colocado en una zona del cerebro (electrodo activo) y otro en una zona neutra, como el lóbulo de la oreja (electrodo de referencia). Es la forma más común y sencilla de registro, y la que usaremos en el laboratorio.

* Bipolar:
  Se colocan dos electrodos en diferentes zonas del cerebro y se mide la diferencia de voltaje entre ellos. Sirve para comparar la actividad entre dos áreas.

* Laplaciana:
  Es parecida a la monopolar, pero en lugar de usar un solo electrodo de referencia, se usa el promedio de varios que rodean al electrodo activo. Esto da una señal más precisa, pero es más compleja y no se usará en esta práctica.
<p align="center"> <img src="IMÁGENES Y VIDEOS/imagen_3.jpg" width="60%" /></p>
<p align="center"> Figura 4. Montaje para registro: (a) Monopolar (b) Bipolar.[5]</p>


### ¿De qué forma obtenemos la señal? <a name="id4"></a>
---
En el laboratorio  de EEG se utilizo el kit de bitalino   y 3 electrodos
## **Objetivos** <a name="id5"></a>
- Establecer un conocimiento teórico y práctico sobre la utilización y adquisición de señales EEG.
- Adquirir señales EEG biomédicas

---

<h2><a name="id6"></a>Materiales y equipos</h2>

<div align="center">

| **Descripción**       | **Cantidad** |
|-----------------------|:------------:|
| Kit BITalino          |      1       |
| Laptop                |      1       |
| Electrodos con gel    |      3       |

</div>
<p align="center"> <img src="IMÁGENES Y VIDEOS/kit_bitalino" width="60%" /></p>


<h2><a name="id7"></a>Procedimiento</h2>



### **Procedimiento** <a name="id7"></a>

*A continuación se describen los pasos realizados durante el laboratorio para la adquisición de señales EEG utilizando el sistema BITalino:*

1. Se preparó el área de trabajo, asegurando un entorno sin ruidos eléctricos ni movimientos innecesarios.  
2. Se limpió con alcohol la piel en los puntos de colocación de los electrodos para mejorar la conductividad.  
3. Se conectó el sensor EEG de BITalino al módulo principal mediante los pines correspondientes (IN+, IN− y referencia).  
4. Se colocaron dos electrodos en la frente (zona **FP1 o FP2**, según la prueba) y un electrodo de referencia detrás de la oreja.  
5. Se conectó el dispositivo BITalino a la laptop mediante Bluetooth y se abrió el software **OpenSignals (r)evolution**.  
6. Se configuró el software con una frecuencia de muestreo de al menos **100 Hz**, adecuada para capturar ondas cerebrales hasta 50 Hz.  
7. Se inició la grabación con el sujeto relajado, en posición cómoda, evitando movimientos faciales, parpadeos o tensión muscular.



### **Protocolo de adquisición** <a name="id9"></a>



La adquisición de señales EEG con el sistema BITalino se llevó a cabo utilizando electrodos de gel autoadhesivos conectados al sensor EEG ensamblado y gestionado a través del software OpenSignals. El objetivo fue registrar la actividad cerebral bajo diferentes condiciones controladas, siguiendo una secuencia experimental definida.

A continuación, se describe detalladamente el procedimiento realizado:
 <p align="center"> <img src="IMÁGENES Y VIDEOS/imagen_1.jpg" width="50%" /></p>
    
<p align="center"> Figura 6. Colocación de electrodos EEG del Bitalino. </p>

#### **Configuración inicial**

- Se conectó el sensor EEG al canal correspondiente del BITalino.
- Se colocaron **dos electrodos activos** en la región frontal de la cabeza: **FP1 y FP2**, de acuerdo con el sistema 10-20 internacional.
- Se colocó el **electrodo de referencia** en la región ósea detrás de la oreja (mastoides).
- Se verificó la conectividad vía **Bluetooth** con el software OpenSignals y se ajustó la frecuencia de muestreo.

#### **Secuencia de registro (12 minutos)**

<div align="center">

| **Minuto** | **Condición**      | **Detalle**                                                        |
|:----------:|:------------------:|:------------------------------------------------------------------:|
| 0–1        | Basal 1            | Ojos abiertos, fijar la vista en un punto fijo                     |
| 1–2        | Basal 2            | Ojos cerrados                                                      |
| 2–4        | Tarea cognitiva    | Restar 7 desde 100 en silencio o realizar cálculos mentales        |
| 4–6        | Artefactos         | Parpadear cada 2 segundos y masticar                               |
| 6–12       | Libre              | Actividad de preguntas de cultura general de todo tipo             |

</div>
#### Notas importantes durante la adquisición**

- Durante las condiciones **basales**, se buscó registrar actividad con la menor cantidad posible de artefactos musculares y oculares.
- En la **tarea cognitiva**, se esperó un incremento en la actividad beta asociada al esfuerzo mental.
- En la fase de **artefactos**, se introdujeron movimientos controlados (parpadeo y masticación) para identificar su efecto en la señal.
- En la fase **libre**, el grupo diseñó una condición personalizada, la cual fue utilizada para comparar los efectos en distintas bandas de frecuencia cerebral.





Cabe mencionar que el procedimiento se repitió en diferentes sujetos de estudio.

 
## **Resultados** <a name="id10"></a>


___
### 1. **Fotos de conexión usada** <a name="id11"></a>
### 1. <strong>Fotos de conexión usada</strong> <a name="id11"></a>

<p align="center"> <img src="IMÁGENES Y VIDEOS/Electrodos_lateral" width="60%" /></p>
<p align="center">Figura 8. Posición de los electrodos en el sujeto de prueba - Vista lateral).</p>

<p align="center"> <img src="IMÁGENES Y VIDEOS/Electrodos_total" width="60%" /></p>
<p align="center">Figura 8. Posición de los electrodos en el  sujeto de prueba - Vista general.</p>

<p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="40%"></p>
<p align="center">Figura 8. Posición de los electrodos en el Bitalino (vista frontal).</p>

<p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="40%"></p>
<p align="center">Figura 9. Posición de los electrodos en el Bitalino (vista lateral).</p>

<p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="40%"></p>
<p align="center">Figura 10. Posición de los electrodos del ULTRACORTEX "MARK IV" (vista posterior).</p>

<p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="40%"></p>
<p align="center">Figura 11. Posición de los electrodos del ULTRACORTEX "MARK IV" (vista posterior).</p>




### 2. **Señal con Bitalino** <a name="id14"></a>
| Etapa                 | Indicaciones                                                                                                       | Toma             |
|-----------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|
| Basal 1 (60 segundos)  | Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos. |<video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/82d554cf-76bf-4a84-bcb8-3286cde2dcd5" width="80%" height="80%"></video> |
| Basal 2 (60 segundos)   | Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos.       | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/8a0fa139-4ad7-46d0-9675-700ebbd0c155" width="50%" height="50%"></video> |
| Tarea cognitiva( 2 minutos) | Registre otra fase de referencia de 30 segundos                                                              | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/ad29e4ad-b436-4184-9fb4-75859c0570c3" width="50%" height="50%"></video> |
| Artefactos(2 minutos) | Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos (*) y resuelve cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos. | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/e48396e2-c8de-45c2-9273-54a04c8cb4a1" width="50%" height="50%"></video> |
| Preguntas complejas(6 minutos) | Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos (*) y resuelve cada uno de ellos mentalmente enfocando tu mirada en un punto específico para evitar artefactos. | <video src="https://github.com/AndreaRazuriMadrid/intro-senales-biomedicas/assets/157930025/e48396e2-c8de-45c2-9273-54a04c8cb4a1" width="50%" height="50%"></video> |
####  **Análisis de las gráficas** <a name="id16"></a>
| **Etapa**                    | **Análisis de las gráficas**                                                                                                                 | **Resultado**                                                                                       |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Basal 1 (60 segundos)**    | Se observarán ondas alfa predominantes (8–12 Hz) con patrón rítmico y baja interferencia muscular. Ideal para establecer una línea base.     | <p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%"></p>                   |
| **Basal 2 (60 segundos)**    | Se observará un cambio claro en la señal: al abrir los ojos, disminuye la actividad alfa (bloqueo), al cerrarlos vuelve a incrementarse.     | <p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%"></p>                   |
| **Tarea cognitiva (2 minutos)** | Aumenta la actividad beta (13–30 Hz) debido al esfuerzo mental. Picos más irregulares y frecuencia más alta en regiones frontales.             | <p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%"></p>                   |
| **Artefactos (2 minutos)**   | Se detectarán señales contaminadas por parpadeo (oscilaciones lentas) y masticación (ruido de alta frecuencia), no vinculadas a ondas cerebrales. | <p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%"></p>                   |
| **Preguntas complejas (6 minutos)** | Predominio de actividad beta con variaciones posibles por fatiga o distracción (aparición de theta). Puede observarse menor regularidad en la señal. | <p align="center"><img src="IMÁGENES Y VIDEOS/IMAGEN_ONDAS.jpg" width="50%"></p>                   |


releeeeeeeeeeeeeeeennnnnnnnnnnnnnnnnnnnnnnar con eustra dataaaaaaaaaaaaaaaaaaaaaaaaaEn el Bitalino, al realizar la medición, trabajan con un sensor de EEG el cuál brinda la señal medida como la diferencia amplificada entre las dos señales de medición que se filtra con un paso de banda de 0,8-48Hz para eliminar la señales no deseadas.[3]
Asimismo, al considerar la posición de los electrodos del Bitalino los cuales fueron en fp1 y fp2, estas regiones están relacionadas con diversas funciones cognitivas y emocionales.
De las 5 gráficas la que tiene mayor amplitud es en la que se expone al sujeto a una luz parpadeante luego de tener los ojos vendados por un periodo de tiempo.


## **Conclusiones** <a name="id17"></a>
---
- Las oscilaciones de la banda delta están presentes en diferentes fases del sueño. Las ondas theta están asociadas con el área frontal del cerebro y se correlacionan con tareas de metal e indican un mayor poder de banda con mayor dificultad de tarea. Las oscilaciones de la banda alfa reflejan funciones relacionadas con la memoria, el motor y los sentidos.La relajación durante la vigilia puede desencadenar un aumento de la potencia de la banda alfa cuando los ojos están cerrados. En comparación, las ondas alfa se suprimen al abrir los ojos y la actividad física o mental.
Las ondas beta se generan en las regiones posterior y frontal. se correlacionan con pensamiento activo y concentración. Con mayor concentración, las oscilaciones beta se disparan en una frecuencia más rápida. 
- Con respecto al bitalino, la mayor amplitud en las señales EEG durante la exposición a la luz parpadeante después de tener los ojos vendados podría deberse a la respuesta de frecuencia de parpadeo y la mayor sensibilidad del sistema visual debido a la privación sensorial previa.
    
## **Referencias** <a name="id18"></a>
1. Maimon NB, Molcho L, Intrator N, Lamy D. Single-channel EEG features during n-back task correlate with working memory load. *arXiv preprint* arXiv:2008.04987. 2020. Disponible en: https://arxiv.org/abs/2008.04987
2. Pagnotta MF, Riddle J, D'Esposito M. Multiplexed levels of cognitive control through delta and theta neural oscillations. *J Cogn Neurosci.* 2024 May 1;36(5):916–935. Disponible en: https://pubmed.ncbi.nlm.nih.gov/38319885/
3. Martínez-Molina MP, Valdebenito-Oyarzo G, Soto-Icaza P, Zamorano F, Figueroa-Vargas A. Lateral prefrontal theta oscillations causally drive a computational mechanism underlying conflict expectation and adaptation. *Nat Commun.* 2024;15(1):9858. Disponible en: https://www.nature.com/articles/s41467-024-54244-8
4. Zheng J, Yebra M, Schjetnan AGP, Mosher C, Kalia A, Chung JM, et al. Theta phase precession supports memory formation and retrieval of naturalistic experience in humans. *Nat Hum Behav.* 2024;8(12):1801–1810. Disponible en: https://www.nature.com/articles/s41562-024-01983-9
5. 6. PLUX Wireless Biosignals. EEG Home Guide. *BITalino Documentation* [Internet]. 2022 [citado 2025 may 1]. Disponible en: [https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf)


‌
‌
