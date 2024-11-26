// Validación de formulario de registro
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function (event) {
        const password = document.getElementById('contrasena').value;
        const confirmPassword = document.getElementById('confirm_contrasena').value;
        
        // Validar que las contraseñas coincidan
        if (password !== confirmPassword) {
            event.preventDefault();
            alert('Las contraseñas no coinciden.');
        }
    });
});
