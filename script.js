// Common validation logic for all pages
function validateForm(event) {
    const inputs = event.target.querySelectorAll('input, textarea');
    for (const input of inputs) {
        if (!input.checkValidity()) {
            alert(`Please fill out the ${input.name || 'required'} field correctly.`);
            input.focus();
            event.preventDefault();
            return false;
        }
    }
    return true;
}

// Attach validation to all forms on the page
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    for (const form of forms) {
        form.addEventListener('submit', validateForm);
    }
});
