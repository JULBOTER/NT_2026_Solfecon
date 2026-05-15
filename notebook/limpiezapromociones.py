import pandas as pd
def limpiar_datospromo(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

# 1. Limpiando los textos para eliminar espacios y garantizar que el primera letra este en mayuscula y el resto minuscula
    # Usamos .astype(str) para asegurar que no haya errores de tipo
    data_frame_limpio["descripcionprom"] = data_frame_limpio["descripcionprom"].astype(str).str.strip().str.capitalize()
    


    #2. Limpiando los textos para controlar valores inesperados solo permite los de la lista
    
    valores_esperados_descripcion = ["Navidad", "Saldos", "Productos seguridad", "Sin promoción"]
    data_frame_limpio["descripcionprom"] = data_frame_limpio["descripcionprom"].where(
        data_frame_limpio["descripcionprom"].isin(valores_esperados_descripcion),
        pd.NA
    )
     

    # --- Limpieza de datos numéricos ---

    # 1. VERIFICAR QUE LOS NÚMEROS SEAN NÚMEROS
    data_frame_limpio["idpromocion"]=pd.to_numeric(data_frame_limpio["idpromocion"])
    data_frame_limpio["descuento"]=pd.to_numeric(data_frame_limpio["descuento"])
    
  
    #2. Verifiquemos los valores numéricos esperados
     #Esto elimina automáticamente las filas con NaN en estas columnas
    data_frame_limpio = data_frame_limpio[data_frame_limpio["idpromocion"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["descuento"] >= 0]
   


    # 4. ELIMINAR REGISTROS VACÍOS
    # Elimina los registros vacios de los campos obligatorios en este caso idpromocion no es obligatorio por eso se reflejan N/A
    columnas_obligatorias = ["idpromocion",  "descuento","descripcionprom","imagen"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio
