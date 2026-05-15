# notebook/exportar.py
import os

RUTA_DATOS = "resultados/datos/"

def exportar_json(preguntas):
    os.makedirs(RUTA_DATOS, exist_ok=True)

    for nombre, df in preguntas.items():
        ruta = os.path.join(RUTA_DATOS, f"{nombre}.json")
        df.to_json(ruta, orient="records", force_ascii=False, indent=2)
        print(f"✅ Exportado: {ruta}")

# Al final de notebook/exportar.py
def exportar_kpis(df_productos, df_lineas, df_promociones):
    import json
    os.makedirs(RUTA_DATOS, exist_ok=True)
    kpis = {
        "total_productos":     int(df_productos["idproducto"].count()),
        "total_lineas":        int(df_lineas["idlinea"].count()),
        "total_promociones":   int(df_promociones["idpromocion"].count()),
        "precio_promedio":     round(float(df_productos["precio"].mean()), 2),
        "precio_maximo":       round(float(df_productos["precio"].max()), 2),
        "precio_minimo":       round(float(df_productos["precio"].min()), 2),
        "suma_total_precios":  round(float(df_productos["precio"].sum()), 2),
    }
    with open(RUTA_DATOS + "kpis.json", "w", encoding="utf-8") as f:
        json.dump(kpis, f, indent=2, ensure_ascii=False)
    print("✅ kpis.json exportado")        