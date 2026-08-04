/* 
   TRUSTIA — Milli Otonomi Platformu (v2.0 Askeri Sınıf)
   Canlı İnteraktif Taktik Konsol Simülatörü (HTML5 Canvas Engine)
*/

document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("tacticalCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  // Set crisp HD resolution
  canvas.width = 900;
  canvas.height = 450;

  // State
  let ugv = { x: 150, y: 225, yaw: 0, targetX: 750, targetY: 225, speed: 2.5 };
  let hazards = [
    { x: 350, y: 200, type: "IED_MINE", radius: 45 },
    { x: 550, y: 260, type: "CBRN_GAS", radius: 60 }
  ];
  let isSimulating = true;

  function drawGrid() {
    ctx.strokeStyle = "rgba(0, 240, 255, 0.08)";
    ctx.lineWidth = 1;
    const step = 30;
    for (let x = 0; x < canvas.width; x += step) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, canvas.height);
      ctx.stroke();
    }
    for (let y = 0; y < canvas.height; y += step) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(canvas.width, y);
      ctx.stroke();
    }
  }

  function drawHazards() {
    hazards.forEach(h => {
      // Pulse animation
      const time = Date.now() * 0.003;
      const pulseR = h.radius + Math.sin(time) * 4;

      ctx.beginPath();
      ctx.arc(h.x, h.y, pulseR, 0, Math.PI * 2);
      ctx.fillStyle = h.type === "IED_MINE" ? "rgba(255, 46, 77, 0.15)" : "rgba(245, 158, 11, 0.15)";
      ctx.fill();
      ctx.strokeStyle = h.type === "IED_MINE" ? "#ff2e4d" : "#f59e0b";
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Label
      ctx.fillStyle = h.type === "IED_MINE" ? "#ff2e4d" : "#f59e0b";
      ctx.font = "10px Space Grotesk, sans-serif";
      ctx.fillText(`[KARANTİNA: ${h.type}]`, h.x - 35, h.y - h.radius - 5);
    });
  }

  function drawUgv() {
    // Draw Planned Path
    ctx.beginPath();
    ctx.moveTo(ugv.x, ugv.y);

    // Simple A* Waypoint Bypass around hazards
    let waypointX = (ugv.x + ugv.targetX) / 2;
    let waypointY = ugv.y < 225 ? 120 : 330;
    ctx.quadraticCurveTo(waypointX, waypointY, ugv.targetX, ugv.targetY);
    ctx.strokeStyle = "rgba(0, 240, 255, 0.6)";
    ctx.setLineDash([6, 6]);
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.setLineDash([]);

    // Target Marker
    ctx.beginPath();
    ctx.arc(ugv.targetX, ugv.targetY, 8, 0, Math.PI * 2);
    ctx.strokeStyle = "#00f0ff";
    ctx.lineWidth = 2;
    ctx.stroke();

    // UGV Icon
    ctx.save();
    ctx.translate(ugv.x, ugv.y);
    ctx.rotate(ugv.yaw);

    // Vehicle Body
    ctx.fillStyle = "#3b82f6";
    ctx.strokeStyle = "#00f0ff";
    ctx.lineWidth = 2;
    ctx.fillRect(-15, -10, 30, 20);
    ctx.strokeRect(-15, -10, 30, 20);

    // LiDAR Field Beam
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.arc(0, 0, 80, -Math.PI / 4, Math.PI / 4);
    ctx.fillStyle = "rgba(0, 240, 255, 0.12)";
    ctx.fill();

    ctx.restore();
  }

  function update() {
    if (!isSimulating) return;

    // Smooth movement towards target along bypass curve
    let dx = ugv.targetX - ugv.x;
    let dy = ugv.targetY - ugv.y;
    let dist = Math.sqrt(dx * dx + dy * dy);

    if (dist > 5) {
      // Avoid hazard dynamically
      let avoidY = 0;
      hazards.forEach(h => {
        let hdx = h.x - ugv.x;
        let hdy = h.y - ugv.y;
        let hdist = Math.sqrt(hdx * hdx + hdy * hdy);
        if (hdist < h.radius + 40) {
          avoidY = h.y > ugv.y ? -1.5 : 1.5;
        }
      });

      ugv.x += (dx / dist) * ugv.speed;
      ugv.y += (dy / dist) * ugv.speed + avoidY;
      ugv.yaw = Math.atan2(dy + avoidY * 10, dx);
    } else {
      // Loop back
      ugv.x = 100;
      ugv.y = 225;
    }
  }

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawGrid();
    drawHazards();
    drawUgv();
    update();
    requestAnimationFrame(render);
  }

  // Interactive Click to Set Goal
  canvas.addEventListener("click", (e) => {
    const rect = canvas.getBoundingClientRect();
    ugv.targetX = e.clientX - rect.left;
    ugv.targetY = e.clientY - rect.top;
  });

  render();
});
