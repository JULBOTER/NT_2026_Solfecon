# notebook/analisis.py
import pandas as pd

def aplicar_analisisrelaciones(df_productos, df_lineas, df_promociones):

    # ─── Merges base (se hacen una sola vez) ──────────────────────────────────
    prod_linea = df_productos.merge(
        df_lineas[["idlinea", "descripcionlinea"]],
        on="idlinea",
        how="left"
    )

    prod_promo = df_productos.merge(
        df_promociones[["idpromocion", "descripcionprom"]],
        on="idpromocion",
        how="left"
    )

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 1: ¿Cuántos productos hay por cada PROMOCIÓN?
    # ══════════════════════════════════════════════════════════════════════════
    filtro1 = prod_promo.query("idpromocion == idpromocion")
    agrupacion1 = (
        filtro1
        .groupby(["idpromocion", "descripcionprom"])["idproducto"]
        .count()
        .reset_index(name="cantidad_productos")
        .sort_values("idpromocion")
    )
    print("\n═══ P1: Cantidad de productos por promoción ═══")
    print(agrupacion1)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 2: ¿Cuántos productos hay por cada LÍNEA?
    # ══════════════════════════════════════════════════════════════════════════
    filtro2 = prod_linea.query("idlinea == idlinea")
    agrupacion2 = (
        filtro2
        .groupby(["idlinea", "descripcionlinea"])["idproducto"]
        .count()
        .reset_index(name="cantidad_productos")
        .sort_values("idlinea")
    )
    print("\n═══ P2: Cantidad de productos por línea ═══")
    print(agrupacion2)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 3: Suma de precios por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro3 = prod_linea.query("precio > 0 and idlinea == idlinea")
    agrupacion3 = (
        filtro3
        .groupby(["idlinea", "descripcionlinea"])["precio"]
        .sum()
        .reset_index(name="suma_precios")
        .sort_values("idlinea")
    )
    print("\n═══ P3: Suma de precios por línea ═══")
    print(agrupacion3)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 4: Promedio de precios por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro4 = prod_linea.query("precio > 0 and idlinea == idlinea")
    agrupacion4 = (
        filtro4
        .groupby(["idlinea", "descripcionlinea"])["precio"]
        .mean()
        .reset_index(name="promedio_precio")
        .sort_values("idlinea")
    )
    agrupacion4["promedio_precio"] = agrupacion4["promedio_precio"].round(2)
    print("\n═══ P4: Promedio de precios por línea ═══")
    print(agrupacion4)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 5: Suma de precios por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro5 = prod_promo.query("precio > 0 and idpromocion == idpromocion")
    agrupacion5 = (
        filtro5
        .groupby(["idpromocion", "descripcionprom"])["precio"]
        .sum()
        .reset_index(name="suma_precios")
        .sort_values("idpromocion")
    )
    print("\n═══ P5: Suma de precios por promoción ═══")
    print(agrupacion5)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 6: Promedio de precios por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro6 = prod_promo.query("precio > 0 and idpromocion == idpromocion")
    agrupacion6 = (
        filtro6
        .groupby(["idpromocion", "descripcionprom"])["precio"]
        .mean()
        .reset_index(name="promedio_precio")
        .sort_values("idpromocion")
    )
    agrupacion6["promedio_precio"] = agrupacion6["promedio_precio"].round(2)
    print("\n═══ P6: Promedio de precios por promoción ═══")
    print(agrupacion6)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 7: Precio MÁXIMO por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro7 = prod_linea.query("precio > 0 and idlinea == idlinea")
    agrupacion7 = (
        filtro7
        .groupby(["idlinea", "descripcionlinea"])["precio"]
        .max()
        .reset_index(name="precio_maximo")
        .sort_values("idlinea")
    )
    print("\n═══ P7: Precio máximo por línea ═══")
    print(agrupacion7)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 8: Precio MÍNIMO por cada LÍNEA
    # ══════════════════════════════════════════════════════════════════════════
    filtro8 = prod_linea.query("precio > 0 and idlinea == idlinea")
    agrupacion8 = (
        filtro8
        .groupby(["idlinea", "descripcionlinea"])["precio"]
        .min()
        .reset_index(name="precio_minimo")
        .sort_values("idlinea")
    )
    print("\n═══ P8: Precio mínimo por línea ═══")
    print(agrupacion8)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 9: Precio MÁXIMO por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro9 = prod_promo.query("precio > 0 and idpromocion == idpromocion")
    agrupacion9 = (
        filtro9
        .groupby(["idpromocion", "descripcionprom"])["precio"]
        .max()
        .reset_index(name="precio_maximo")
        .sort_values("idpromocion")
    )
    print("\n═══ P9: Precio máximo por promoción ═══")
    print(agrupacion9)

    # ══════════════════════════════════════════════════════════════════════════
    # PREGUNTA 10: Precio MÍNIMO por cada PROMOCIÓN
    # ══════════════════════════════════════════════════════════════════════════
    filtro10 = prod_promo.query("precio > 0 and idpromocion == idpromocion")
    agrupacion10 = (
        filtro10
        .groupby(["idpromocion", "descripcionprom"])["precio"]
        .min()
        .reset_index(name="precio_minimo")
        .sort_values("idpromocion")
    )
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