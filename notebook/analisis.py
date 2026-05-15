# notebook/analisis.py
import pandas as pd

def aplicar_analisis(df_productos):

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 1: ¿Cuántos productos hay por cada PROMOCIÓN?
    # ══════════════════════════════════════════════════════════════════════════
    filtro1 = df_productos.query("idpromocion == idpromocion")  # excluye nulos
    agrupacion1 = filtro1.groupby("idpromocion")["idproducto"].count().reset_index(name="cantidad_productos")
    print("\n═══ P1: Cantidad de productos por promoción ═══")
    print(agrupacion1)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 2: ¿Cuántos productos hay por cada LÍNEA?
    # ══════════════════════════════════════════════════════════════════════════
    filtro2 = df_productos.query("idlinea == idlinea")  # excluye nulos
    agrupacion2 = filtro2.groupby("idlinea")["idproducto"].count().reset_index(name="cantidad_productos")
    print("\n═══ P2: Cantidad de productos por línea ═══")
    print(agrupacion2)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 3: Suma de precios por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro3 = df_productos.query("precio > 0 and idlinea == idlinea")
    agrupacion3 = filtro3.groupby("idlinea")["precio"].sum().reset_index(name="suma_precios")
    print("\n═══ P3: Suma de precios por línea ═══")
    print(agrupacion3)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 4: Promedio de precios por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro4 = df_productos.query("precio > 0 and idlinea == idlinea")
    agrupacion4 = filtro4.groupby("idlinea")["precio"].mean().reset_index(name="promedio_precio")
    agrupacion4["promedio_precio"] = agrupacion4["promedio_precio"].round(2)
    print("\n═══ P4: Promedio de precios por línea ═══")
    print(agrupacion4)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 5: Suma de precios por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro5 = df_productos.query("precio > 0 and idpromocion == idpromocion")
    agrupacion5 = filtro5.groupby("idpromocion")["precio"].sum().reset_index(name="suma_precios")
    print("\n═══ P5: Suma de precios por promoción ═══")
    print(agrupacion5)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 6: Promedio de precios por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro6 = df_productos.query("precio > 0 and idpromocion == idpromocion")
    agrupacion6 = filtro6.groupby("idpromocion")["precio"].mean().reset_index(name="promedio_precio")
    agrupacion6["promedio_precio"] = agrupacion6["promedio_precio"].round(2)
    print("\n═══ P6: Promedio de precios por promoción ═══")
    print(agrupacion6)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 7: Precio MÁXIMO por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro7 = df_productos.query("precio > 0 and idlinea == idlinea")
    agrupacion7 = filtro7.groupby("idlinea")["precio"].max().reset_index(name="precio_maximo")
    print("\n═══ P7: Precio máximo por línea ═══")
    print(agrupacion7)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 8: Precio MÍNIMO por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro8 = df_productos.query("precio > 0 and idlinea == idlinea")
    agrupacion8 = filtro8.groupby("idlinea")["precio"].min().reset_index(name="precio_minimo")
    print("\n═══ P8: Precio mínimo por línea ═══")
    print(agrupacion8)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 9: Precio MÁXIMO por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro9 = df_productos.query("precio > 0 and idpromocion == idpromocion")
    agrupacion9 = filtro9.groupby("idpromocion")["precio"].max().reset_index(name="precio_maximo")
    print("\n═══ P9: Precio máximo por promoción ═══")
    print(agrupacion9)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 10: Precio MÍNIMO por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro10 = df_productos.query("precio > 0 and idpromocion == idpromocion")
    agrupacion10 = filtro10.groupby("idpromocion")["precio"].min().reset_index(name="precio_minimo")
    print("\n═══ P10: Precio mínimo por promoción ═══")
    print(agrupacion10)

    # ─── Retornar todas las agrupaciones ─────────────────────────────────────
    return {
        "p1_cantidad_por_promocion":     agrupacion1,
        "p2_cantidad_por_linea":         agrupacion2,
        "p3_suma_precios_linea":         agrupacion3,
        "p4_promedio_precios_linea":     agrupacion4,
        "p5_suma_precios_promocion":     agrupacion5,
        "p6_promedio_precios_promocion": agrupacion6,
        "p7_precio_max_linea":           agrupacion7,
        "p8_precio_min_linea":           agrupacion8,
        "p9_precio_max_promocion":       agrupacion9,
        "p10_precio_min_promocion":      agrupacion10,
    }