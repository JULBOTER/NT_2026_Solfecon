import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

  #rutina para evaluar textos
    #seleccionar todas  las columnas de tipo texto y eliminar sus espacios y poner en minuscula
    columnas_texto = ["id","descripcion"] 
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype("string").str.strip().str.lower()

 #rutina para evaluar fechas
    #evaluar que una fechas si es una fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])

    #reemplazar una fecha por fefecto si el campo llega vacio
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)


    #rutina para evaluar imagenes
    #evaluar que las imagenes no lleguen vacias y si llegan vacias colocar
    data_frame_limpio["imagen"] = data_frame_limpio["imagen"].fillna("/img/imagen_default.jpg")

   