import { useState } from "react";

export default function Home() {
  const [q, setQ]       = useState("");
  const [a, setA]       = useState("");
  const [busy, setBusy] = useState(false);

  const ask = async () => {
    setBusy(true);
    const r = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: q })
    });
    const { answer } = await r.json();
    setA(answer);
    setBusy(false);
  };

  const makePodcast = async () => {
    setBusy(true);
    const r = await fetch("/api/podcast", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: q })
    });
    const { download } = await r.json();
    window.open(download, "_blank");
    setBusy(false);
  };

  return (
    <main style={{ 
      padding: "32px", 
      fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
      background: "linear-gradient(135deg, #1a1a2e 0%, #0f0f23 100%)",
      minHeight: "100vh",
      color: "#ffffff"
    }}>
      <div style={{
        maxWidth: "800px",
        margin: "0 auto",
        background: "rgba(255, 255, 255, 0.05)",
        borderRadius: "16px",
        padding: "40px",
        backdropFilter: "blur(10px)",
        border: "1px solid rgba(255, 255, 255, 0.1)"
      }}>
        <h1 style={{
          fontSize: "2.5rem",
          marginBottom: "30px",
          background: "linear-gradient(90deg, #4c9aff 0%, #764ce8 100%)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent"
        }}>Heritage Artifact POC</h1>
        
        <div style={{ marginBottom: "20px" }}>
          <input 
            style={{ 
              width: "100%", 
              padding: "15px",
              fontSize: "16px",
              borderRadius: "8px",
              border: "1px solid rgba(255, 255, 255, 0.2)",
              background: "rgba(255, 255, 255, 0.1)",
              color: "#ffffff",
              marginBottom: "15px"
            }} 
            value={q} 
            onChange={e => setQ(e.target.value)} 
            placeholder="Ask about your ancestors..." 
          />
          
          <div style={{ display: "flex", gap: "10px" }}>
            <button 
              onClick={ask} 
              disabled={busy}
              style={{
                padding: "12px 24px",
                borderRadius: "8px",
                border: "none",
                background: busy ? "#666" : "linear-gradient(90deg, #4c9aff 0%, #764ce8 100%)",
                color: "#ffffff",
                fontSize: "16px",
                cursor: busy ? "not-allowed" : "pointer",
                transition: "all 0.3s ease"
              }}
            >
              {busy ? "Processing..." : "Ask"}
            </button>
            
            <button 
              onClick={makePodcast} 
              disabled={busy}
              style={{
                padding: "12px 24px",
                borderRadius: "8px",
                border: "2px solid #4c9aff",
                background: "transparent",
                color: "#4c9aff",
                fontSize: "16px",
                cursor: busy ? "not-allowed" : "pointer",
                transition: "all 0.3s ease"
              }}
            >
              Make Podcast
            </button>
          </div>
        </div>
        
        {a && (
          <div style={{ 
            background: "rgba(255, 255, 255, 0.05)",
            borderRadius: "8px",
            padding: "20px",
            marginTop: "30px",
            border: "1px solid rgba(255, 255, 255, 0.1)"
          }}>
            <pre style={{ 
              whiteSpace: "pre-wrap", 
              fontFamily: "monospace",
              fontSize: "14px",
              lineHeight: "1.6",
              margin: 0,
              color: "#e0e0e0"
            }}>{a}</pre>
          </div>
        )}
      </div>
    </main>
  );
}