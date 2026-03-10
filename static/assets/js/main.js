document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    const successMessage = document.getElementById('success-message');

    // If this script runs on a page without the contact form, do nothing
    if (!form) {
        return;
    }

    form.addEventListener('submit', function(e) {
        e.preventDefault();  // sayfa reload'u engelle

        // form verilerini al
        const formData = new FormData(form);
        const csrfTokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
        const csrfToken = csrfTokenInput ? csrfTokenInput.value : '';

        // Use the form's action attribute, which Django already rendered
        fetch(form.action, {
            method: "POST",
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        })
        .then(response => {
            if(response.ok) {
                successMessage.style.display = "block";
                form.reset(); 
            } else {
                alert("Something went wrong");
            }
        })
        .catch(error => console.error(error));
    });
});