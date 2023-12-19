"""
El codigo corresponde a un trabajo en proceso para poder realizar detecciones a tiempo real utilizando
vision computacional.
No corresponde a un formato final ni en estado de ser liberado al publico para su utilizacion formal.
"""
########################################################################################################
# Vision computacional #################################################################################
########################################################################################################

# Importar librerias de ultralytics
from ultralytics import YOLO
import cv2

# Leer modelo entrenado
model = YOLO("best.pt")

# Deteccion con camara
cap = cv2.VideoCapture(0)

# Iteracion de deteccion
while True:
    ret, frame = cap.read()
    resultados = model.predict(frame, imgsz=640, conf=0.98)
    anotaciones = resultados[0].plot()
    cv2.imshow("Deteccion de plagas", anotaciones)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

########################################################################################################
# Notas de autor #######################################################################################
########################################################################################################
"""
Uso bajo discrecion propia.
La division no se hace responsable por los resultados utilizacion de este codigo, esta queda bajo 
responsabilidad de quien utilize el codigo
"""
