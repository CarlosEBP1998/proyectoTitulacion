const express = require('express');
const cors = require('cors');

const app = express();

app.use(express.static('public'));
app.use(cors());
app.use(express.json());

//VALIDACION DE DOCUMENTOS;

//INVOCAR MODULOS DE PYTHON Y PASAR COMO PARAMETROS LOS DOCUMENTOS;

app.listen(8080, () => {
    console.log("Servidor en marcha");
});