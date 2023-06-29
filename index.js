const express = require('express');
const cors = require('cors');
const {exec} = require('child_process');
const mysql = require('mysql2');

const app = express();

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'master',
    password: '12345',
    database: 'users'
});

app.use(express.static('public'));
app.use(cors());
app.use(express.json());

//LOGIN

app.post("/login", (req, res) => {

    const usuarioId = req.body.usuario || "";
    const password = req.body.password || "";

    console.log("Usuario:" + usuarioId);
    console.log("Password: " + password);

    connection.connect((error) => {
        if (error) {
          console.error('Error de conexión: ' + error.stack);
          return;
        }
        console.log('Conexión a la base de datos exitosa');
    });

    connection.query(`SELECT nombre_Usuario, passw FROM USUARIO WHERE nombre_Usuario = '${usuarioId}' && passw = '${password}'`, function (error, results, fields) {
        if (error) {
          console.log('Hubo un error: ' + error);
        }
        else if( results.length > 0){
          res.setHeader("Access-Control-Allow-Origin", "*");

          exec('streamlit run ./modulosPython/INICIO.py', (err, stdout, stderr) => {
            res.send(stdout);
          });
          
          res.send({respuesta: 'encontrado'});
        }
        else {
          res.setHeader("Access-Control-Allow-Origin", "*")
          res.send({respuesta: 'error'})
        }
    });

    //
})

//OTRAS

app.get('/calculos', (req, res) => {

    // exec('python3 ./modulosPython/Main_pruba.py', (err, stdout, stderr) => {
    //     res.send(stdout);
    // });

    exec('streamlit run ./modulosPython/INICIO.py', (err, stdout, stderr) => {
         res.send(stdout);
    });
});

//VALIDACION DE DOCUMENTOS;

//INVOCAR MODULOS DE PYTHON Y PASAR COMO PARAMETROS LOS DOCUMENTOS;

app.listen(8080, () => {
    console.log("Servidor en marcha");
});