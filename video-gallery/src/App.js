import { useState } from 'react';

function App() {
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(false);
  // NEW: track the currently playing video's embed URL
  const [playingUrl, setPlayingUrl] = useState(null);

  const fetchVideos = async () => {
    setLoading(true);
    try {
      const resp = await fetch("http://localhost:8000/videos");
      const data = await resp.json();
      setVideos(data.videos);
    } catch (err) {
      console.error(err);
      alert("Failed to load videos");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <button onClick={fetchVideos} disabled={loading}>
        {loading ? "Loading…" : "Load YouTube Videos"}
      </button>

      {/* Grid of thumbnails */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))",
        gap: 16,
        marginTop: 20
      }}>
        {videos.map(v => (
          <div key={v.url} style={{ cursor: "pointer" }}
               onClick={() => setPlayingUrl(v.url + "?autoplay=1")}>
            <img
              src={v.thumbnail}
              alt={v.title}
              style={{ width: "100%", borderRadius: 8 }}
            />
            <div style={{ marginTop: 8, fontSize: "0.9rem" }}>
              {v.title}
            </div>
          </div>
        ))}
      </div>

      {/* Conditional embed player */}
      {playingUrl && (
        <div style={{
          position: "fixed",
          top: 0, left: 0, right: 0, bottom: 0,
          background: "rgba(0,0,0,0.8)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          zIndex: 1000
        }}>
          <div style={{ position: "relative", width: "80%", maxWidth: 800 }}>
            <button
              onClick={() => setPlayingUrl(null)}
              style={{
                position: "absolute",
                top: -30, right: 0,
                fontSize: 24,
                background: "transparent",
                border: "none",
                color: "#fff",
                cursor: "pointer"
              }}
            >
              ✕
            </button>
            <iframe
              width="100%"
              height="450"
              src={playingUrl}
              frameBorder="0"
              allow="autoplay; encrypted-media"
              allowFullScreen
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
