import { useState, useEffect } from "react";
import KPICard from "./components/KPICard";
import GraficaImagen from "./components/GraficaImagen";

const graficas = [
  { src: "/graficas/g1_pie_productos_por_promocion.png", pregunta: "P1", titulo: "Cantidad de productos por promoción", conclusion: "Muestra qué promoción agrupa más productos del catálogo, permitiendo identificar cuál es la estrategia promocional más aplicada." },
  { src: "/graficas/g2_barras_productos_por_linea.png", pregunta: "P2", titulo: "Cantidad de productos por línea", conclusion: "Identifica qué línea concentra más productos, útil para decisiones de abastecimiento e inventario." },
  { src: "/graficas/g3_barras_suma_precios_linea.png", pregunta: "P3", titulo: "Suma de precios por línea", conclusion: "Evidencia qué línea representa el mayor valor económico total acumulado en el inventario." },
  { src: "/graficas/g4_scatter_promedio_linea.png", pregunta: "P4", titulo: "Precio promedio por línea", conclusion: "Visualiza las líneas con precios promedio más altos, útil para estrategias de pricing diferenciado." },
  { src: "/graficas/g5_barras_suma_precios_promocion.png", pregunta: "P5", titulo: "Suma de precios por promoción", conclusion: "Indica qué promoción agrupa productos de mayor valor acumulado, orientando la gestión de descuentos." },
  { src: "/graficas/g6_barras_promedio_promocion.png", pregunta: "P6", titulo: "Precio promedio por promoción", conclusion: "Compara el precio promedio entre promociones, revelando si los descuentos aplican a productos de alto o bajo valor." },
  { src: "/graficas/g7_lineas_precio_max_linea.png", pregunta: "P7", titulo: "Precio máximo por línea", conclusion: "Destaca qué líneas tienen los productos más costosos, ayudando a segmentar el portafolio por precio." },
  { src: "/graficas/g8_lineas_precio_min_linea.png", pregunta: "P8", titulo: "Precio mínimo por línea", conclusion: "Identifica qué líneas ofrecen productos más accesibles, útil para estrategias de precio de entrada." },
  { src: "/graficas/g9_barras_precio_max_promocion.png", pregunta: "P9", titulo: "Precio máximo por promoción", conclusion: "Revela qué promoción contiene los productos más costosos, orientando la selección de artículos para cada campaña." },
  { src: "/graficas/g10_barras_precio_min_promocion.png", pregunta: "P10", titulo: "Precio mínimo por promoción", conclusion: "Muestra qué promoción incluye los productos más baratos, permitiendo evaluar la accesibilidad de cada campaña." }
];

const kpisConfig = [
  { key: "total_productos",    titulo: "Total productos",        color: "#1565C0", icono: "📦" },
  { key: "total_lineas",       titulo: "Líneas disponibles",     color: "#2E7D32", icono: "🗂️" },
  { key: "total_promociones",  titulo: "Promociones activas",    color: "#E65100", icono: "🏷️" },
  { key: "precio_promedio",    titulo: "Precio promedio",        color: "#6A1B9A", icono: "💰" },
  { key: "precio_maximo",      titulo: "Precio más alto",        color: "#C62828", icono: "📈" },
  { key: "precio_minimo",      titulo: "Precio más bajo",        color: "#00838F", icono: "📉" },
  { key: "suma_total_precios", titulo: "Valor total inventario", color: "#4527A0", icono: "🏪" },
];

function formatValor(key, valor) {
  if (valor === null || valor === undefined) return "...";
  if (["precio_promedio","precio_maximo","precio_minimo","suma_total_precios"].includes(key))
    return "$" + Number(valor).toLocaleString("es-CO", { maximumFractionDigits: 0 });
  return valor;
}

function App() {
  const [kpis, setKpis] = useState(null);

  useEffect(() => {
    fetch("/datos/kpis.json")
      .then(r => r.json())
      .then(setKpis)
      .catch(() => console.error("No se pudo cargar kpis.json"));
  }, []);

  return (
    <div style={{ minHeight: "100vh", background: "#f0f2f5", fontFamily: "'Segoe UI', Arial, sans-serif" }}>

      {/* ENCABEZADO */}
      <div style={{ background: "linear-gradient(135deg, #1565C0, #0D47A1)", color: "white", padding: "28px 40px", marginBottom: "36px" }}>
        <h1 style={{ margin: 0, fontSize: "2rem" }}>🔧 Dashboard Ferretería SOLFECON</h1>
        <p style={{ margin: "6px 0 0", opacity: 0.85 }}>Análisis de productos, líneas y promociones</p>
      </div>

      <div style={{ padding: "0 40px 60px" }}>

        {/* KPIs */}
        <h2 style={{ color: "#1a1a2e", marginBottom: "20px" }}>📊 Indicadores clave</h2>
        <div style={{ display: "flex", gap: "16px", flexWrap: "wrap", marginBottom: "48px" }}>
          {kpisConfig.map(k => (
            <KPICard
              key={k.key}
              titulo={k.titulo}
              valor={formatValor(k.key, kpis?.[k.key])}
              color={k.color}
              icono={k.icono}
            />
          ))}
        </div>

        {/* GRÁFICAS */}
        <h2 style={{ color: "#1a1a2e", marginBottom: "20px" }}>📈 10 Preguntas de negocio</h2>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(500px, 1fr))", gap: "28px" }}>
          {graficas.map((g, i) => (
            <GraficaImagen key={i} src={g.src} pregunta={g.pregunta} titulo={g.titulo} conclusion={g.conclusion} />
          ))}
        </div>

      </div>
    </div>
  );
}

export default App;