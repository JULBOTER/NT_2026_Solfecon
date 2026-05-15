import pandas as pd
def limpiar_datoslinea(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

# 1. Limpiando los textos para eliminar espacios y garantizar que el primera letra este en mayuscula y el resto minuscula
    # Usamos .astype(str) para asegurar que no haya errores de tipo
    data_frame_limpio["descripcionlinea"] = data_frame_limpio["descripcionlinea"].astype(str).str.strip().str.capitalize()
    


    #2. Limpiando los textos para controlar valores inesperados solo permite los de la lista
    
    valores_esperados_descripcion = ["Pinturas y accesorios", "Construcción", "Plomería y gas", "Eléctricos","Agropecuario","Herramientas","Seguridad industrial","Limpieza y accesorios","Adhesivos y empaques","Tornillería y accesorios","Abrasivos y químicos","Herrajes y cerrajería"]

    data_frame_limpio["descripcionlinea"] = data_frame_limpio["descripcionlinea"].where(
        data_frame_limpio["descripcionlinea"].isin(valores_esperados_descripcion),
        pd.NA
    )
     

    # --- Limpieza de datos numéricos ---

    # 1. VERIFICAR QUE LOS NÚMEROS SEAN NÚMEROS
    data_frame_limpio["idlinea"]=pd.to_numeric(data_frame_limpio["idlinea"])
    
  
    #2. Verifiquemos los valores numéricos esperados
     #Esto elimina automáticamente las filas con NaN en estas columnas
    data_frame_limpio = data_frame_limpio[data_frame_limpio["idlinea"] > 0]

   


    # 4. ELIMINAR REGISTROS VACÍOS
    # Elimina los registros vacios de los campos obligatorios 
    columnas_obligatorias = ["idlinea",  "descripcionlinea","imagen"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio

