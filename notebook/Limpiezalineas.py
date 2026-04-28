import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # ---- LIMPIEZA NUMÉRICA ----
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio = data_frame_limpio.dropna(subset=["id"])
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    # ---- LIMPIEZA DE TEXTO ----
    columnas_texto = ["descripcion"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = (
            data_frame_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    # eliminar descripciones vacías
    data_frame_limpio = data_frame_limpio[data_frame_limpio["descripcion"] != ""]

    # ---- LIMPIEZA DE IMÁGENES ----
    data_frame_limpio["imagen"] = data_frame_limpio["imagen"].fillna("/img/imagen_default.jpg")

    # ---- CAMPOS OBLIGATORIOS ----
    columnas_obligatorias = ["id", "descripcion", "imagen"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # ---- DUPLICADOS ----
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
