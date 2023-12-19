"""
El codigo corresponde a un recopilado del originalmente desarrollado en "jupyter notebook".
La idea es poder acceder a los codigos de manera directa.
"""
########################################################################################################
# Imports en google colaboratory #######################################################################
########################################################################################################

# Obtener directorios (o carpetas mejor dicho) de google drive
from google.colab import drive
drive.mount('/content/drive')

# Obtener archivos de la carpeta de google drive
from google.colab import files
files.download("/content/weights.zip")

########################################################################################################
# Instalacion de Yolo ##################################################################################
########################################################################################################

# Instalacion de yolov8
%pip install ultralytics

# Importar la libreria de ultralytics, desarrollador de yolov8 y donde se encuentra la herramienta en
# cuestion
import ultralytics
ultralytics.checks()

########################################################################################################
# Entrenamiento en yolov8 ##############################################################################
########################################################################################################

# Para entrenamiento en google colaboratory
import os
import sys
os.environ["PYTHONPATH"]="/content/drive/MyDrive/YOLOv8"

# Codigo para entrenar la red, modelo general
"""
!yolo train model=yolov8m.pt data=/content/drive/MyDrive/Datasets/YOLODataset/dataset.yaml epochs=100 imgsz=640 conf=0.5

model: version de yolo con que se quiere entrenar
data: direccion del archivo en formato .yaml del dataset que se quiere entrenar
epochs: cantidad de epocas de entrenamiento
imgsz: Imagen de deteccion en este caso
conf: 'confiansa' en los resultados, cualquier valor menor al insertado se descarta como resultado
"""

# Ejemplo para el modelo yolov8m, con 30 epocas, imagen de 640 pixeles de tamano
!yolo train model=yolov8m.pt data=/content/drive/MyDrive/Datasets/YOLODataset/dataset.yaml epochs=30 imgsz=640 optimizer=Adamax

########################################################################################################
# Revision y descargas #################################################################################
########################################################################################################

# Para obtencion de resultados
!yolo predict model='/content/runs/detect/train13/weights/best.pt' source='/content/drive/MyDrive/Paulo/cydia_44/cydia_44/12.jpeg' conf=0.9

# Guardar en un archivo comprimido los resultados
!zip -r "/content/drive/MyDrive/Datasets/entrenamientos_yyyyt" "/content/runs"

########################################################################################################
# Notas de autor #######################################################################################
########################################################################################################
"""
Cualquier error ortografico, se omitieron caracteres como 'tildes' para evitar algun colapso en python.
"""


