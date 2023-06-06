const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const uploadStatus = document.getElementById('upload-status');

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



