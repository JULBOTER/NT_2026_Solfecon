# notebook/exportar.py
import os

RUTA_DATOS = "resultados/datos/"

def exportar_json(preguntas):
    os.makedirs(RUTA_DATOS, exist_ok=True)

    for nombre, df in preguntas.items():
        ruta = os.path.join(RUTA_DATOS, f"{nombre}.json")
        df.to_json(ruta, orient="records", force_ascii=False, indent=2)
        print(f"✅ Exportado: {ruta}")