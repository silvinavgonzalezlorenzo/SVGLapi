
const URL = "http://localhost:5000"
const documento = document.getElementById('registroClub');

documento.addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(documento); // Obtener los datos del formulario

    fetch(URL + '/socios', { // Enviar los datos al servidor
        method: 'POST', // Metodo de envio
        body: formData // Los datos del formulario
    })
     .then(res => res.json()) // Convertir la respuesta a JSON
     .then(data => { // Mostrar los datos en consola
        console.log(data);
        alert('Socio agregado correctamente');
        window.location.href = 'index.html' // Redireccionar a index.html
    })

})
