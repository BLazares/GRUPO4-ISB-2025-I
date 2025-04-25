# **LABORATORIO 4: – Uso de BiTalino para EMG y ECG**


# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     4.1 [Conexión usada](#id5)\
     4.2 [Video de la señal](#id6)\
     4.3 [Ploteo de la señal en OpenSignal](#id7)\
     4.4 [Archivos](#id8)\
     4.5 [Ploteo de la señal en Python](#id9)
6. [Conclusiones](#id10)
7. [Referencias](#id11)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify">
El electrocardiograma (ECG) es una herramienta fundamental en la medicina moderna que permite registrar la actividad eléctrica del corazón a lo largo del tiempo. Esta actividad eléctrica es esencial para la contracción coordinada del músculo cardíaco, y su análisis proporciona información valiosa sobre el estado fisiológico del corazón .
</p>
<p align="justify">
El trazado típico de un ECG consta de varias ondas y complejos que representan diferentes fases del ciclo cardíaco: la onda P indica la despolarización auricular, el complejo QRS refleja la despolarización ventricular, y la onda T corresponde a la repolarización ventricular . La interpretación adecuada de estos componentes es crucial para el diagnóstico de diversas patologías cardíacas, como arritmias, infartos de miocardio y otras condiciones que afectan la conducción eléctrica del corazón.</p>


<p align="center">
     <p align="center"><img src="datos/CORAZON_PQRST.gif" width="400"></p>


---

### ⚡ Componentes del Electrocardiograma (ECG)

<p align="justify">
El electrocardiograma (ECG) es una herramienta de diagnóstico que permite registrar la actividad eléctrica del corazón a través de un conjunto de ondas, segmentos e intervalos. Cada uno de estos componentes representa distintos eventos fisiológicos del ciclo cardíaco. Comprender su significado es esencial para interpretar correctamente el trazado del ECG.
</p>


| Componente     | Descripción |
|----------------|-------------|
| **Onda P**     | Representa la despolarización auricular, es decir, el impulso eléctrico que activa las aurículas. |
| **Complejo QRS** | Refleja la despolarización ventricular. Incluye la activación del tabique interventricular (Q), masa ventricular principal (R), y regiones finales (S). |
| **Onda T**     | Representa la repolarización de los ventrículos, preparándolos para el siguiente ciclo. |
| **Segmento PR** | Tiempo entre el final de la onda P y el inicio del QRS; muestra la conducción desde aurículas a ventrículos. |
| **Segmento ST** | Pausa eléctrica entre la despolarización y repolarización ventricular; útil para detectar isquemia. |
| **Intervalo PR** | Desde el inicio de la onda P hasta el inicio del QRS; indica el tiempo total de conducción auriculoventricular. |
| **Intervalo QT** | Incluye QRS, ST y T; muestra la duración total de la despolarización y repolarización ventricular. |
| **Intervalo RR** | Distancia entre dos ondas R consecutivas; se utiliza para calcular la frecuencia cardíaca. |



<p align="center">
  <img src="datos/PQRST.png" width="400">
</p>
<p align="center">
Figura 1. Componentes de un EKG
</p>

### ❓ ¿Cómo se interpreta el ECG?

<p align="justify">
El electrocardiograma (ECG) permite identificar la actividad eléctrica del corazón mediante la medición de diferentes ondas e intervalos. La siguiente tabla resume la interpretación y valores fisiológicos normales de cada componente del ECG, junto con sus respectivas imágenes.
</p>

| Componente        | Interpretación                                                                                     | Imagen |
|------------------|-----------------------------------------------------------------------------------------------------|--------|
| **Onda P**        | - Despolarización auricular  <br> - Duración: ~0.12 s <br> - Amplitud: ~0.25 mV                     | <img src="datos/ONDAP.png" width="200"><br><sub>Figura 2. Onda P</sub> |
| **Intervalo PR**  | - Desde el inicio de la onda P hasta el inicio del QRS  <br> - Duración: 0.12 – 0.20 s              | <img src="datos/INTERVARLOPR.jpg" width="200"><br><sub>Figura 3. Intervalo PR</sub> |
| **Complejo QRS**  | - Despolarización ventricular  <br> - Duración: ~0.10 s  <br> - Evalúa bloqueos y arritmias         | <img src="datos/PQRST.png" width="200"><br><sub>Figura 4. Complejo QRS</sub> |
| **Segmento ST**   | - Pausa entre despolarización y repolarización ventricular  <br> - Alteraciones indican isquemia    | <img src="datos/Segmento-ST.jpg" width="200"><br><sub>Figura 5. Segmento ST</sub> |
| **Onda T**        | - Repolarización ventricular  <br> - Altura: &lt;5 mm (frontales), &lt;15 mm (precordiales)         | <img src="datos/ONDAT.jpg" width="200"><br><sub>Figura 6. Onda T</sub> |
| **Intervalo RR**  | - Tiempo entre dos ondas R consecutivas  <br> - Se usa para calcular la frecuencia cardíaca         | <img src="datos/INTERVALORR.png" width="200"><br><sub>Figura 7. Intervalo RR</sub> |
| **Intervalo QT**  | - Desde inicio del QRS hasta final de onda T  <br> - QTc normal: hasta 450 ms (H), 470 ms (M)       | <img src="datos/intervalo_qt.jpg" width="200"><br><sub>Figura 8. Intervalo QT</sub> |



## **Objetivos** <a name="id1"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution 


## **Materiales y equipos** <a name="id2"></a>

---
<div align="center">

|  **Imagen**  | **Producto** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| <img width="200" height="150" src="https://i.postimg.cc/VvLXqb8P/14022-01a.jpg"> |   Kit BITalino  |       1      |
| <img width="200" height="150" src="https://i.postimg.cc/XNmdLX3Z/equipos.png"> |      Laptop     |       1      |
| <img width="200" height="150" src="https://multimedia.3m.com/mws/media/277491J/eletrodo-2239.jpg?width=506"> |      Electrodos    |       5     |

</div>



## **Procedimiento** <a name="id3"></a>


Para la colocación de los electrodos se siguió la guía oficial de BITalino: *"BITalino HOME-GUIDE #2: ELECTROCARDIOGRAPHY (ECG) - Exploring Cardiac Signals at the Skin Surface"*.

La señal ECG se registró dos veces en cada uno de los siguientes estados:

- **Estado basal**: reposo completo.  
- **Respiración controlada**: ciclos de inhalación y exhalación de 15 segundos.  
- **Ejercicio intenso**: actividad física durante 6 minutos.  
- **Respiración prolongada**: apnea involuntaria hasta ahogarse.  

---



## **Resultados** <a name="id4"></a>

### **Conexión usada** <a name="id5"></a>
#


Se posicionaron los electrodos en base las guías mencionadas:
<p align="center"><img src="https://user-images.githubusercontent.com/89707896/231556282-5514bddb-7edd-44c2-b25a-eff7b03f8c3e.png" width="500" height="200"></p>
<p align="center">Figura 6. Posición de los electrodos según la guía.

<p align="center"><img src="https://user-images.githubusercontent.com/55772705/231652569-8c111952-0d50-4b4b-83f3-a2abce33c01e.PNG" width="400" height="400"></p>
<p align="center">Figura 7. Muestra una configuración del sensor de ECG BiTalino para la derivación I de Einthoven.
    

### 🎥 Videos de la adquisición organizados por condición

### 🎥 Videos de la adquisición organizados por condición y derivada

| Condición              | Derivada           | Primer muestreo                                               | Segundo muestreo                                              |
|------------------------|--------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| **Estado basal**       | Primera derivada   | <video src="https://user-images.githubusercontent.com/89707896/231572641-61aeebae-f397-4627-aebc-913bb9464915.mp4" width="200" controls></video> | <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Resp. controlada**   | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Ejercicio intenso**  | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Resp. prolongada**   | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |



### **Ploteo de la señal en OpenSignal** <a name="id7"></a>

| Condición              | Derivada           | Primer muestreo                                               | Segundo muestreo                                              |
|------------------------|--------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| **Estado basal**       | Primera derivada   | <video src="https://user-images.githubusercontent.com/89707896/231572641-61aeebae-f397-4627-aebc-913bb9464915.mp4" width="200" controls></video> | <video src="https://user-images.githubusercontent.com/89707896/231574043-44222491-d595-4d5a-9ac8-112adb20757c.mp4" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Resp. controlada**   | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Ejercicio intenso**  | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
| **Resp. prolongada**   | Primera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Segunda derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |
|                        | Tercera derivada   | <video src="#" width="200" controls></video>                  | <video src="#" width="200" controls></video>                  |

### **Archivos** <a name="id8"></a>
Se encuentran en la carpeta del laboratorio 4.
#
### **Ploteo de la señal en Python** <a name="id9"></a>

<p align="justify">
a) Estado basal  
Se observa el complejo QRS el cual indica un tiempo corto de despolarización de los ventrículos, lo que indicaría un corto periodo de movimiento dentro de estas cavidades. Asimismo, se observa una alta presencia de ruido en la región del ST, además existe una especie de pendiente en el segmento isoeléctrico lo que indicaría algo de actividad en el ventrículo incluso cuando no hay electricidad fluyendo a través de él. Por último también se llegaría a notar una onda T, representativa de la repolarización de los ventrículos. [5]
</p>

| Ploteo del primer intento | Ploteo del segundo intento |
|---------------------------|----------------------------|
| <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612373-866789aa-8ddd-477b-8046-dcdd2fb0a006.jpeg"><br><sub>Figura 12. Señal en estado basal</sub> | <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654224-cf1270e8-7896-4804-8997-df66e2c907c8.jpeg"><br><sub>Figura 13. Señal en estado basal (FFT)</sub> |

     


     b)   Manteniendo la respiración por 10 segundos
La inspiración profunda puede generar cambios tanto en la posición como en la orientación del corazón a través de un desplazamiento hacia abajo del diafragma que afectan la señal ECG. Estos cambios pueden observarse entre los 35 a 45 segundos en la siguiente gráfica [6].
 
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612494-7170cc27-7967-43cf-8a9a-4b9723d330b5.jpeg">
</p>
<p align="center">
Figura 14. Ploteo de la señal en Python manteniendo la respiración por 10 segundos
</p>           
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654465-896baf32-5ccf-4387-bcfe-8d5befcd8ab7.jpeg">
</p>
<p align="center">
Figura 15. Ploteo de la señal en Python manteniendo la respiración por 10 segundos FFT.
</p> 

     c)   Reposo basal
En la interpretación de la señal en el reposo basal tras la respiración se puede observar una onda P superior al estado basal por lo que se puede deducir que en este caso existe una mayor despolarización auricular indicando mayor movimiento en estas cavidades debido a la recepción de sangre por parte del corazón. Posteriormente observamos una mayor amplitud entre los picos R y S dentro del complejo QRS lo que indicaría que existiría una mayor actividad en las ventriculas esto debido al mayor volumen de sangre que habían recibido las aurículas previamente antes de pasar por las válvulas. Por último, también son visibles las ondas T teniendo una alta actividad debido a la gran actividad llevada a cabo por los ventrículos previamente [5]  
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618112-00da6811-468e-44a0-b59b-3a21ff3e670c.jpeg">
</p>
<p align="center">
Figura 16. Ploteo de la señal en Python en reposo basal
</p>     
     
  
     d)   Después de una actividad física
El aumento de frecuencia cardiaca debido al ejercicio físico desencadena cambios en la señal ECG como una mayor amplitud de la onda Q, disminución del intervalo RR, ondas T altas y puntiagudas, superposición de ondas P y ondas T [7].
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231612958-916cd9ab-8c21-4a5a-b14c-873c48aaed8d.jpeg">
</p>
<p align="center">
Figura 17. Ploteo de la señal en Python después de una actividad física
</p>

<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231613142-dc8be0b0-f355-47f7-a7de-9e24b72ab6c3.jpeg">
</p>
<p align="center">
Figura 18. Ploteo de la señal en Python después de una actividad física
</p>
   
  
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231654949-05231391-82a7-4dbd-87be-86b448262199.jpeg">
</p>
<p align="center">
Figura 19. Ploteo de la señal en Python despues de una actividad física FFT.
</p> 


      e)Simulacion
En la simulación del ejercicio son visibles la mayoría de segmentos y ondas de los dos estados anteriores, sin embargo, en este es visible, además de la falta de ruido, existe una menor diferencia entre los picos R y el  S dentro del complejo QRS en comparación a los datos obtenidos de la voluntaria en cuyo caso la diferencia es mucho mayor. También se puede notar una bastante visible y prolongada, que va de acuerdo a los altos picos dentro del segmento QRS. [5]
<p align="center">
     <img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231618251-0bdaa1b1-8cef-4617-b91a-030c0d1a37d3.jpeg">
</p>
<p align="center">
Figura 20. Ploteo de la simulación.
</p>

<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231655079-c854059d-2adf-4521-9d37-49811f2a2b9b.jpeg">
</p>
<p align="center">
Figura 21. Ploteo de la señal en Python de la simulación FFT.
</p> 

## Analisis de las gráficas FFT 
Las gráficas de FFT obtenidas experimentalmente (estado de reposo, respiración profunda y post ejercicio) son muy similares entre sí. Sin embargo, al compararlas con el simulador se puede observar la diferencia en el rango inicial del espectro. Aproximadamente, entre 0-25 Hz. Se ha comprobado que esta respuesta a la frecuencia es la que se debería obtener al filtrar la señal de forma correcta. Artículos indican que la forma de la densidad espectral es similar. Como se puede observar en la tercera gráfica, en la que se realizó un estudio acerca de la fft de la señal ECG en la primera derivación (DI).

<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/55772705/231656084-6ae8dd1b-83f4-4a09-a60f-dd0eefe56aad.PNG">
</p>
<p align="center">
Figura 22. Representación de la densidad espectral de Potencia en DI [9].
</p> 


## **Conclusiones** <a name="id10"></a>
-1) Estado de reposo: 
Se puede observar que la grafica obtenida de la simulacion y la parte experimental son parecidas ,por lo que se estima que el rango del valor del la frecuencia cardiaca de la persona estudiada esta en el rango normal de 60 a 100 lpm,el cual es el valor de una persona sana.Asi mismo el desempeño de la tarea el ritmo cardiaco se regularizaba significativamente de acuerdo a los valores obtenidos en condiciones de reposo.
</p>
-2)Estado de respiracion profunda:
Durante la respiración la morfología del latido esta influencia por dos mecanismos ,los cambios en la impedancia torácica y la orientación del eje eléctrico del corazón con respecto a los electrodos ECG,por lo la frecuencia cardiaca está en el rango de 60-100 lpm y la frecuencia respiratoria está en el rango de 15 -60 respiraciones por minuto.Por lo cual se debe apreciar un cambio en el espectro obtenido ,lo cual sucede en el segundo 40 ,ya que se puede apreciar en la gráfica un descenso cuando la persona empieza a tomar aire y lo contiene y hay un aumento cuando ella libera el oxígeno y vuelve a la respiración continua.

</p>
-3)Estado despues de la actividad fisica:
En este caso las frecuencia cardiacas de interés son la frecuencia cardiaca máxima y la frecuencia cardiaca mínima,ya que se puede corroborar con la primera el reflejo del trabajo anaeróbico producido por el ejercicio realizado.De igual forma ocurre con la frecuencia mínima,ya que está debe estar en los valores del intervalo de recuperación ,del estado basal.En este caso se obtuvo una cambio notorio en la amplitud de los picos de las señal obtenida en el estado de actividad física  teniendo un valor alrededor de 615 como máximo y mínimo de 350, lo cual supera los valores del estado de reposo que fueron de  570 como maximo y minimo de 360.

## **Referencias** <a name="id11"></a>
----
<p align="justify">
1. Electrocardiograma. (2023, 28 de febrero). MedlinePlus. https://medlineplus.gov/spanish/pruebas-de-laboratorio/electrocardiograma/#:~:text=Un%20electrocardiograma%20(ECG)%20es%20un,circula%20a%20través%20de%20él.
</p>
<p align="justify">
2. Electrocardiograma: MedlinePlus enciclopedia médica. (2022, 5 de agosto). MedlinePlus - Health Information from the National Library of Medicine. https://medlineplus.gov/spanish/ency/article/003868.htm#:~:text=No%20haga%20ejercicio%20ni%20tome,acciones%20pueden%20causar%20resultados%20falsos.
</p>
<p align="justify">
3. Cascino, T., & Shea, M. J. (2021, 6 de julio). Electrocardiografía - Trastornos del corazón y los vasos sanguíneos - Manual MSD versión para público general. Manual MSD versión para público general. https://www.msdmanuals.com/es-es/hogar/trastornos-del-corazón-y-los-vasos-sanguíneos/diagnóstico-de-las-enfermedades-cardiovasculares/electrocardiografía#:~:text=En%20un%20ECG%20pueden%20observarse,las%20pareces%20del%20músculo%20cardíaco.
</p>
<p align="justify">
4. ECG interpretation: Characteristics of the normal ECG (P-wave, QRS complex, ST segment, T-wave). (2019). ECG & ECHO. https://ecgwaves.com/topic/ecg-normal-p-wave-qrs-complex-st-segment-t-wave-j-point/
</p>
<p align="justify">
5. S. Kurisu, K. Nitta, Y. Sumimoto, H. Ikenaga, K. Ishibashi, Y. Fukuda, and Y. Kihara, “Effects of deep inspiration on QRS axis, T-wave axis and frontal QRS-T angle in the routine electrocardiogram,” Heart and Vessels, vol. 34, no. 9, pp. 1519–1523, 2019.
</p>
<p align="justify">
6. G. P. Whyte and S. Sharma, Practical ECG for Exercise Science and Sports Medicine. Champaign, IL: Human Kinetics, 2010.
</p>
<p align="justify">
7. E. A. Rosas, Electrocardiografía Clínica. Ciudad de México: El Manual Moderno, 2017.
</p>
<p align="justify">
8. Guardado R. Vallín D., (2009, 2 de junio). Aplicación del Análisis Tiempo-Frecuencia en Electrocardiografía. https://laccei.org/LACCEI2009-Venezuela/Papers/IT117_GuardadoMedina.pdf
</p>
