const URL = "http://localhost:5000"



fetch(URL + '/socios') // Obtener los socios
    .then(res => res.json()) // Convertir la respuesta a JSON
    .then(data => { // Mostrar los datos en consola
       let html = ''; // Variable para guardar el HTML

       data.forEach(element => {
        //Bucktick `` para concatenar, interpolacion de variables ${}
        html = html + `<tr> 
            <td>${element[0]}</td>
            <td>${element[1]}</td>
            <td>${element[2]}</td>
            <td>${element[3]}</td>
            <td>${element[4]}</td>
            <td>${element[5]}</td>

            <td><a href="modificar.html?idsisclub=${element[0]}">Modificar</a></td>
            <td><button class="alert" onclick="eliminar(${element[0]});">Eliminar</button></td>
        </tr>`;
       });

       document.getElementById('socios').innerHTML = html;
    });


function eliminar(id){

    fetch(URL + '/socios/' + id, { // Hago la petición a la API para eliminar el socio
        method: 'DELETE' // Indico el método HTTP
    }).then(res => res.json()) // Convierto la respuesta a JSON
    .then(data => {
        console.log(data); // Muestro los datos en consola
        alert('Socio eliminado: ' + id); // Muestro un mensaje al usuario
        window.location.reload(); // Recargo la página
    });


}