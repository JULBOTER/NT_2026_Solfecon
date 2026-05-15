function GraficaImagen({ src, titulo, pregunta, conclusion }) {
  return (
    <div style={{
      background: "white",
      borderRadius: "16px",
      padding: "24px",
      boxShadow: "0 2px 12px rgba(0,0,0,0.08)"
    }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "12px" }}>
        <span style={{
          background: "#1565C0",
          color: "white",
          borderRadius: "8px",
          padding: "4px 10px",
          fontSize: "0.8rem",
          fontWeight: "bold"
        }}>
          {pregunta}
        </span>
        <h3 style={{ margin: 0, color: "#222", fontSize: "1rem" }}>{titulo}</h3>
      </div>
      <img
        src={src}
        alt={titulo}
        style={{ width: "100%", borderRadius: "10px", border: "1px solid #eee" }}
      />
      <div style={{
        marginTop: "12px",
        background: "#f0f7ff",
        borderLeft: "4px solid #1565C0",
        borderRadius: "6px",
        padding: "12px 16px",
        color: "#444",
        fontSize: "0.88rem"
      }}>
        📌 <strong>Conclusión:</strong> {conclusion}
      </div>
    </div>
  );
}

export default GraficaImagen;