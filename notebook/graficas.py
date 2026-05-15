# notebook/graficas.py
import matplotlib
matplotlib.use('Agg')              # Primero configurar backend
import matplotlib.pyplot as plt    # Luego pyplot
import numpy as np
import os

RUTA_GRAFICAS = "resultados/graficas/"

def generar_graficas(preguntas):
    os.makedirs(RUTA_GRAFICAS, exist_ok=True)

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 1 — PIE: Cantidad de productos por PROMOCIÓN (P1)
    # Conclusión: Muestra qué promoción agrupa más productos del catálogo,
    #             permitiendo identificar cuál es la estrategia más aplicada.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p1_cantidad_por_promocion"]
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        df["cantidad_productos"],
        labels=df["idpromocion"].astype(str),
        autopct="%1.1f%%",
        startangle=140,
        colors=["#FF9800", "#4CAF50", "#E91E63", "#9C27B0", "#2196F3"]
    )
    ax.set_title("P1: Cantidad de productos por promoción", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g1_pie_productos_por_promocion.png", dpi=150)
    plt.close()
    print("✅ Gráfica 1 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 2 — BARRAS: Cantidad de productos por LÍNEA (P2)
    # Conclusión: Identifica qué línea concentra más productos,
    #             útil para decisiones de abastecimiento e inventario.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p2_cantidad_por_linea"]
    fig, ax = plt.subplots(figsize=(11, 5))
    bars = ax.bar(
        df["idlinea"].astype(str),
        df["cantidad_productos"],
        color="#2196F3",
        edgecolor="black"
    )
    ax.bar_label(bars, padding=3, fontsize=9)
    ax.set_title("P2: Cantidad de productos por línea", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Línea")
    ax.set_ylabel("Cantidad de productos")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g2_barras_productos_por_linea.png", dpi=150)
    plt.close()
    print("✅ Gráfica 2 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 3 — BARRAS HORIZONTALES: Suma de precios por LÍNEA (P3)
    # Conclusión: Evidencia qué línea representa el mayor valor económico
    #             total, guiando la priorización del inventario.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p3_suma_precios_linea"]
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(
        df["idlinea"].astype(str),
        df["suma_precios"],
        color="#4CAF50",
        edgecolor="black"
    )
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=8)
    ax.set_title("P3: Suma de precios por línea", fontsize=14, fontweight="bold")
    ax.set_xlabel("Suma de precios ($)")
    ax.set_ylabel("ID Línea")
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g3_barras_suma_precios_linea.png", dpi=150)
    plt.close()
    print("✅ Gráfica 3 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 4 — SCATTER: Promedio de precios por LÍNEA (P4)
    # Conclusión: Visualiza las líneas con precios promedio más altos,
    #             útil para estrategias de pricing diferenciado por línea.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p4_promedio_precios_linea"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.scatter(
        df["idlinea"].astype(str),
        df["promedio_precio"],
        color="#9C27B0",
        s=180,
        zorder=5
    )
    for _, row in df.iterrows():
        ax.annotate(
            f"${row['promedio_precio']:,.0f}",
            (str(row["idlinea"]), row["promedio_precio"]),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=8,
            color="#9C27B0"
        )
    ax.set_title("P4: Precio promedio por línea", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Línea")
    ax.set_ylabel("Precio promedio ($)")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g4_scatter_promedio_linea.png", dpi=150)
    plt.close()
    print("✅ Gráfica 4 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 5 — BARRAS: Suma de precios por PROMOCIÓN (P5)
    # Conclusión: Indica qué promoción agrupa productos de mayor valor
    #             acumulado, orientando la gestión de descuentos.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p5_suma_precios_promocion"]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(
        df["idpromocion"].astype(str),
        df["suma_precios"],
        color="#FF5722",
        edgecolor="black"
    )
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=9)
    ax.set_title("P5: Suma de precios por promoción", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Promoción")
    ax.set_ylabel("Suma de precios ($)")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g5_barras_suma_precios_promocion.png", dpi=150)
    plt.close()
    print("✅ Gráfica 5 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 6 — BARRAS HORIZONTALES: Promedio de precios por PROMOCIÓN (P6)
    # Conclusión: Compara el precio promedio entre promociones, revelando
    #             si los descuentos aplican a productos de alto o bajo valor.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p6_promedio_precios_promocion"]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(
        df["idpromocion"].astype(str),
        df["promedio_precio"],
        color="#03A9F4",
        edgecolor="black"
    )
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=9)
    ax.set_title("P6: Precio promedio por promoción", fontsize=14, fontweight="bold")
    ax.set_xlabel("Precio promedio ($)")
    ax.set_ylabel("ID Promoción")
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g6_barras_promedio_promocion.png", dpi=150)
    plt.close()
    print("✅ Gráfica 6 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 7 — LÍNEAS: Precio MÁXIMO por LÍNEA (P7)
    # Conclusión: Destaca qué líneas tienen los productos más costosos,
    #             ayudando a segmentar el portafolio por nivel de precio.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p7_precio_max_linea"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(
        df["idlinea"].astype(str),
        df["precio_maximo"],
        marker="o",
        color="#F44336",
        linewidth=2.5,
        markersize=8,
        label="Precio máximo"
    )
    for _, row in df.iterrows():
        ax.annotate(
            f"${row['precio_maximo']:,.0f}",
            (str(row["idlinea"]), row["precio_maximo"]),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center',
            fontsize=8,
            color="#F44336"
        )
    ax.set_title("P7: Precio máximo por línea", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Línea")
    ax.set_ylabel("Precio máximo ($)")
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g7_lineas_precio_max_linea.png", dpi=150)
    plt.close()
    print("✅ Gráfica 7 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 8 — LÍNEAS: Precio MÍNIMO por LÍNEA (P8)
    # Conclusión: Permite identificar qué líneas ofrecen productos más
    #             accesibles, útil para estrategias de precio de entrada.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p8_precio_min_linea"]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(
        df["idlinea"].astype(str),
        df["precio_minimo"],
        marker="s",
        color="#2196F3",
        linewidth=2.5,
        markersize=8,
        label="Precio mínimo"
    )
    for _, row in df.iterrows():
        ax.annotate(
            f"${row['precio_minimo']:,.0f}",
            (str(row["idlinea"]), row["precio_minimo"]),
            textcoords="offset points",
            xytext=(0, 8),
            ha='center',
            fontsize=8,
            color="#2196F3"
        )
    ax.set_title("P8: Precio mínimo por línea", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Línea")
    ax.set_ylabel("Precio mínimo ($)")
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g8_lineas_precio_min_linea.png", dpi=150)
    plt.close()
    print("✅ Gráfica 8 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 9 — BARRAS: Precio MÁXIMO por PROMOCIÓN (P9)
    # Conclusión: Revela qué promoción contiene los productos más costosos,
    #             orientando la selección de artículos para cada campaña.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p9_precio_max_promocion"]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(
        df["idpromocion"].astype(str),
        df["precio_maximo"],
        color="#E91E63",
        edgecolor="black"
    )
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=9)
    ax.set_title("P9: Precio máximo por promoción", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Promoción")
    ax.set_ylabel("Precio máximo ($)")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g9_barras_precio_max_promocion.png", dpi=150)
    plt.close()
    print("✅ Gráfica 9 guardada")

    # ══════════════════════════════════════════════════════════════════════════
    # GRÁFICA 10 — BARRAS: Precio MÍNIMO por PROMOCIÓN (P10)
    # Conclusión: Muestra qué promoción incluye los productos más baratos,
    #             permitiendo evaluar la accesibilidad de cada campaña.
    # ══════════════════════════════════════════════════════════════════════════
    df = preguntas["p10_precio_min_promocion"]
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(
        df["idpromocion"].astype(str),
        df["precio_minimo"],
        color="#607D8B",
        edgecolor="black"
    )
    ax.bar_label(bars, fmt="%.0f", padding=3, fontsize=9)
    ax.set_title("P10: Precio mínimo por promoción", fontsize=14, fontweight="bold")
    ax.set_xlabel("ID Promoción")
    ax.set_ylabel("Precio mínimo ($)")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICAS + "g10_barras_precio_min_promocion.png", dpi=150)
    plt.close()
    print("✅ Gráfica 10 guardada")

    print(f"\n🎉 10 gráficas guardadas en: {RUTA_GRAFICAS}")