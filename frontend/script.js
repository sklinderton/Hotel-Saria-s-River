// Consumir reseñas (JSONPlaceholder)
fetch('https://jsonplaceholder.typicode.com/comments?_limit=5')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('reviewContainer');
    data.forEach(r => {
      container.innerHTML += `
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;">
          <h4>${r.name}</h4>
          <p>${r.body}</p>
        </div>`;
    });
  });

// Enviar reservación
document.getElementById('reservationForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;
  const data = {
    name: form.name.value,
    email: form.email.value,
    suite: form.suite.value,
    date: form.date.value
  };

  const res = await fetch('http://localhost:8000/reservations/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert('¡Reservación exitosa!');
    form.reset();
    loadReservations();
  } else {
    alert('Error al enviar la reservación.');
  }
});

// Obtener y mostrar reservaciones
async function loadReservations() {
  const res = await fetch('http://localhost:8000/reservations/');
  const data = await res.json();
  const container = document.getElementById('reservationList');
  container.innerHTML = '';
  data.forEach(r => {
    container.innerHTML += `
      <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;">
        <p><strong>${r.name}</strong> reservó <em>${r.suite}</em> para el <strong>${r.date}</strong></p>
      </div>`;
  });
}

loadReservations();
