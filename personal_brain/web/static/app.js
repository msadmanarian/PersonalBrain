document.addEventListener("DOMContentLoaded", () => {
  initGraph();
  fetchStatus();
});

let nodes = [];
let edges = [];

async function fetchStatus() {
  try {
    const res = await fetch("/api/status");
    const data = await res.json();
    document.getElementById("node-count-indicator").textContent = `Nodes: ${data.nodes_count} | Links: ${data.edges_count}`;
  } catch (err) {
    console.warn(err);
  }
}

async function initGraph() {
  const canvas = document.getElementById("brainCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  try {
    const res = await fetch("/api/graph");
    const data = await res.json();
    const rawNodes = data.nodes || [];
    const count = rawNodes.length;
    nodes = rawNodes.map((n, i) => {
      const angle = (i / (count || 1)) * 2 * Math.PI;
      const radius = 180 + (i % 2) * 60;
      return {
        ...n,
        x: canvas.width / 2 + Math.cos(angle) * radius,
        y: canvas.height / 2 + Math.sin(angle) * radius,
      };
    });
    edges = data.edges || [];
    animate();
  } catch (err) {
    console.error(err);
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    edges.forEach((edge) => {
      const src = nodes.find((n) => n.node_id === edge.source_id);
      const tgt = nodes.find((n) => n.node_id === edge.target_id);
      if (src && tgt) {
        ctx.beginPath();
        ctx.moveTo(src.x, src.y);
        ctx.lineTo(tgt.x, tgt.y);
        ctx.strokeStyle = "rgba(0, 242, 254, 0.25)";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    });
    nodes.forEach((node) => {
      ctx.beginPath();
      ctx.arc(node.x, node.y, 14, 0, 2 * Math.PI);
      ctx.fillStyle = "#00f2fe";
      ctx.shadowColor = "#00f2fe";
      ctx.shadowBlur = 10;
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = "#ffffff";
      ctx.font = "11px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(node.title, node.x, node.y + 24);
    });
    requestAnimationFrame(animate);
  }
}
