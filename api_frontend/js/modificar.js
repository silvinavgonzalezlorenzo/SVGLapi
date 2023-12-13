const URL = "http://localhost:5000"

const queryString = window.location.search; // Obtener la query string de la URL
const urlParams = new URLSearchParams(queryString); // Obtener los parámetros de la query string

const idsisclub = urlParams.get('idsisclub'); // Obtener el código del socio

fetch(URL + '/socios/' + idsisclub) // Obtener el socio
.then(res => res.json()) // Convertir la respuesta a JSON
.then(data => { // Mostrar los datos en consola
    console.log(data);
    document.getElementById('idsisclub').value = data[0];
    document.getElementById('nombre').value = data[1];
    document.getElementById('apellido').value = data[2];
    document.getElementById('tel').value = data[3];
    document.getElementById('ciudad').value = data[4];
    document.getElementById('pais').value = data[5];
});

const documento = document.getElementById('registroClub');

documento.addEventListener('submit', e => {
    e.preventDefault();

    const formData = new FormData(documento); // Obtener los datos del formulario

    fetch(URL + '/socios/' + idsisclub, { // Enviar los datos al servidor
        method: 'POST', // Metodo de envio
        body: formData // Los datos del formulario
    })
     .then(res => res.json()) // Convertir la respuesta a JSON
     .then(data => { // Mostrar los datos en consola
        console.log(data);
        alert('Socio modificado correctamente');
        window.location.reload(); // Recargar la página
    })
})
