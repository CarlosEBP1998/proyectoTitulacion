function pythonModules() {
    fetch('http://localhost:8080/calculos')
        .then((res) => {
            if(res.ok) {
                res.text()
                    .then((respuesta) => {
                        console.log(respuesta);
                    })
            }
        })
}