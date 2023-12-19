"""
Para el etiquetado de imagenes y su posterior uso, fueron necesarias las librerias de python labelme
 y labelme2yolo.
De esta forma, para realizar el proceso se siguieron los siguentes procesos
"""

########################################################################################################
# Etiquetado de imagenes, labelme ######################################################################
########################################################################################################

# Instalacion de libreria labelme
pip install labelme

# Para ejecutar el programa y etiquetar imagenes, disclaimer, es un proceso manual por imagenes
labelme

""""
Este proceso arrojara el dataset que uno desee etiquetar en formato .json, el cual tenemos que 
transformar para poder ser posteriormente interpretado por YOLOv8
"""

########################################################################################################
# Cambio de formato, labelme2yolo ######################################################################
########################################################################################################

# Instalacion de la libreria labelme2yolo
pip install labelme2yolo

# Convertir archivos .json
labelme2yolo --json_dir '/inserte/direccion/del/directorio'

"""
El directorio/carpeta donde se encuentre el dataset que se quiera convertir, debe contener todas las 
imagenes (se hace todo el traspaso de formatos de una) solamente en formato .json, si no, no se ejecutara
"""

########################################################################################################
# Notas de autor #######################################################################################
########################################################################################################

"""
> Para el etiquetado, este se tiene que realizar con el mismo nombre para cada objeto, si no se tendra
deteccion de diferentes objetos.
> Es importante que, utilizar la libreria labelme2yolo, esta se utilize en una carpeta donde solo se tenga
archivos en formato .json, si no, no funcionara
> Una vez convertido el dataset, el resultado sera una carpeta/directorio que tendra que ser reorganizado
separando las imagenes que se utilizaran para entrenar y validar de manera manual, al igual que el archivo
en formato .yaml quedar externo a cualquiera de estos dos. El dataset de prueba corresponde al formato
en que deberia quedar para el optimo uso a la hora de entrenar
"""



