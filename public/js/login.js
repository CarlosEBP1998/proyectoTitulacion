const formulario = document.getElementById('formulario')
formulario.addEventListener('submit', function(event){
    event.preventDefault();
})

function login () {
    const usuarioInput = document.getElementById('userName');
    const passwordInput = document.getElementById('userPass');
    let usuario;
    let password;

    usuario = usuarioInput.value;
    password = passwordInput.value;

    fetch('http://localhost:8080/login', {
        method: "post",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            usuario,
            password
        })
    })
        .then(response => response.json())
        .then(data => {
            if(data.respuesta == 'encontrado'){
                // window.location.href = './Base_2010.html';
                location.reload();
            }
            else{
                alert('USUARIO NO ENCONTRADO');
                location.reload();
            }

        })
        .catch(error => {
            console.log('Error:' + error);
        })
}