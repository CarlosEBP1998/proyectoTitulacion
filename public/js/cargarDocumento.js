const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const uploadStatus = document.getElementById('upload-status');
const chargeButton = document.getElementById('chargeButton');

chargeButton.disabled = true;

fileInput.addEventListener('change', function (){
  console.log(fileInput.files.lenght);
  if(fileInput.files.length > 0){
    chargeButton.disabled = false;
  }
  else {
    chargeButton.disabled = true;
  }
});

uploadForm.addEventListener('submit', (event) => {
    event.preventDefault();
    
    const file = fileInput.files[0];

    if (file) {
      uploadStatus.textContent = `Cargando: ${file.name}`;

      // Aquí puedes realizar acciones adicionales con el archivo cargado, como enviarlo a un servidor o procesarlo localmente.

      // Limpia el campo de entrada de archivo después de cargar el archivo.
      fileInput.value = '';
    } else {
      uploadStatus.textContent = 'No se seleccionó ningún archivo.';
    }
});



