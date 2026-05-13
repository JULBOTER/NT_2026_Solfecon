import pandas as pd

def limpiar_datospro(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. Limpiando los textos para eliminar espacios y mayúsculas
    # Usamos .astype(str) para asegurar que no haya errores de tipo
    data_frame_limpio["descripcionprod"] = data_frame_limpio["descripcionprod"].astype(str).str.strip().str.lower()
    data_frame_limpio["estado"] = data_frame_limpio["estado"].astype(str).str.strip().str.lower()

    """

    #2. Limpiando los textos para controlar valores inesperados solo permite los de la lista
    valores_esperados_descripcion = ["martillo", "sierra", "cautin", "brocha", "galon de pintura"]
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].where(
        data_frame_limpio["descripcion"].isin(valores_esperados_descripcion),
        pd.NA
    )

    #  Limpiando los textos para controlar valores inesperados solo permite los de la lista
    valores_esperados_estado = ["activo", "inactivo"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(valores_esperados_estado),
        pd.NA
    )

    """

    # --- Limpieza de datos numéricos ---

    # 1. VERIFICAR QUE LOS NÚMEROS SEAN NÚMEROS
    data_frame_limpio["idproducto"]=pd.to_numeric(data_frame_limpio["idproducto"])
    data_frame_limpio["precio"]=pd.to_numeric(data_frame_limpio["precio"])
    

    # 2. Verifiquemos los valores numéricos esperados
    # Esto elimina automáticamente las filas con NaN en estas columnas
    data_frame_limpio = data_frame_limpio[data_frame_limpio["idproducto"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["precio"] >= 100]
   

    #3. Reemplazar idlinea vacío por un código por defecto
    valor_default = 1
    data_frame_limpio["idlinea"] = data_frame_limpio["idlinea"].fillna(valor_default)

    # 4. ELIMINAR REGISTROS VACÍOS
    # Elimina los registros vacios de los campos obligatorios en este caso idpromocion no es obligatorio por eso se reflejan N/A
    columnas_obligatorias = ["idproducto", "descripcionprod", "precio", "estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio
