function KPICard({ titulo, valor, color, icono }) {
  return (
    <div style={{
      background: color,
      borderRadius: "16px",
      padding: "28px 24px",
      color: "white",
      textAlign: "center",
      boxShadow: "0 6px 20px rgba(0,0,0,0.15)",
      flex: "1",
      minWidth: "160px"
    }}>
      <div style={{ fontSize: "2.4rem", marginBottom: "8px" }}>{icono}</div>
      <div style={{ fontSize: "2rem", fontWeight: "bold", marginBottom: "6px" }}>
        {valor}
      </div>
      <div style={{ fontSize: "0.85rem", opacity: 0.9 }}>
        {titulo}
      </div>
    </div>
  );
}

export default KPICard;