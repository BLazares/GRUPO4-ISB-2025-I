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
*fundamentos*
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

*insertar imagen emg*
<p align="justify">
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/bit-con2.jpg" width="400" height="266"></p>
</p>

y este fue conectado a 3 electrodos. Uno negro negativo, uno rojo positivo y uno blanco de referencia. Por lo que las señales ....[]
*insertar imagen conexiones*


Siguiendo la guía ... elaborada por ....se colocaron los electrodos EMG en ... []

*Posición de los electrodos deltoides*
*Posición de los electrodos bíceps*

### **MEDICIONES EN DELTOIDES** <a name="id5"></a>

<p align="justify">
Se tomaron señales del músculo en reposo y contracción.Presione el icono de video rojo para acceder a la lista de reproducción de la primera prueba.<br>
     
</p>
<p align="center"><img src="/.png" width="400" height="300"></p>
*insertar imagen *
<div align="center">

|  **Reposo**  | **Movimiento ligero** | **Fuerza** |
|:------------:|:---------------:|:------------:|
|<video src="https://user-images.githubusercontent.com/62686249/231337697-050966ab-cd84-454a-b6eb-9ab720da62cd.mp4"></video>|<video src="https://user-images.githubusercontent.com/62686249/231337782-f487bdb1-d614-4010-8caa-26c267cba7f6.mp4"></video>|<video src= "https://user-images.githubusercontent.com/62686249/231337918-3db1b3f2-4e32-4e3c-bb6f-f8fb607a03d2.mp4"></video>|

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://www.youtube.com/playlist?list=PLZDUFkiHuQKhex5qfmNXrVl5pFNnRhcRX)

</div>

### **MEDICIONES EN BICEPS BRAQUIAL** <a name="id6"></a>

<p align="justify">
Se tomo señales del reposo y contracción del músculo.Presione el icono de video rojo para acceder a la lista de reproducción de la primera prueba.<br>
     
</p>
<p align="center"><img src="/.png" width="400" height="300"></p>
*insertar imagen *
<div align="center">

|  **Reposo**  | **Movimiento ligero** | **Fuerza** |
|:------------:|:---------------:|:------------:|
|<video src="https://user-images.githubusercontent.com/62686249/231337697-050966ab-cd84-454a-b6eb-9ab720da62cd.mp4"></video>|<video src="https://user-images.githubusercontent.com/62686249/231337782-f487bdb1-d614-4010-8caa-26c267cba7f6.mp4"></video>|<video src= "https://user-images.githubusercontent.com/62686249/231337918-3db1b3f2-4e32-4e3c-bb6f-f8fb607a03d2.mp4"></video>|

[<img src="https://cdn.icon-icons.com/icons2/1713/PNG/512/iconfinder-videologoplayicon-3993847_112649.png" width="20%" height="20%">](https://www.youtube.com/playlist?list=PLZDUFkiHuQKhex5qfmNXrVl5pFNnRhcRX)

</div>

### **Archivos** <a name="id7"></a>
- [Documentos (.txt)](https://github.com/Grupo2-IntroduccionSenalesMedicas/S_biomedica/tree/main/Documentos/BiTalino)
- [Programa de ploteo (Jupyter Notebook)](https://github.com/Grupo2-IntroduccionSenalesMedicas/S_biomedica/blob/main/Programaci%C3%B3n/Laboratorio%203/SignalPlot.ipynb)

## **Resultados y limitaciones** <a name="id7"></a>


### **Video de la señal y ploteo en Opensignal** <a name="id6"></a>

### **Ploteo de la señal en Python** <a name="id8"></a>
<p align="justify">
La primera prueba se realizo con el dedo pulgar en el cuál se tomaron muestras del dedo en reposo, contra fuerza y en posición de pinza con el dedo índice.
</p>
- Señal de dedo con contrafuerza:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_dedo_contrafuerza.jpg" width="800" height="500"></p>
- Señal de dedo en posición de pinza:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_dedo_pinza.jpg" width="800" height="500"></p>

En la segunda prueba se realizó con el biceps del brazo el cual se sometio a contra fuerza y contracción máxima.
</p>
- Señal de biceps en contracción:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_biceps_contraccion.jpg" width="800" height="500"></p>
- Señal de biceps con contrafuerza:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_biceps_contrafuerza.jpg" width="800" height="500"></p>

En la tercera prueba, el usuario estuvo en posición sentado y parado, y de las dos formas se sometió a contracción el músculo gastrocnemio.
</p>
- Señal de contracción del gastrocnemio en posición parado:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_pantorrilla_parado.jpg" width="800" height="500"></p>
- Señal de contracción del gastrocnemio en posición sentado:
<p align="center"><img src="/ISB/Laboratorios/Imagenes/Bitalino/EMG_Python_pantorrilla_sentado.jpg" width="800" height="500"></p>

## **Referencias** <a name="id9"></a>
