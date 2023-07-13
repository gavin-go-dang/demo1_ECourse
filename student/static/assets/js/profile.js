
const fullNameInput = document.querySelector('input[name="full_name"]');

const emailInput = document.querySelector('input[name="email"]');

const updateButton = document.querySelector('input[name="update"]');

fullNameInput.addEventListener('input', function () {
    updateButton.removeAttribute('disabled');
});

emailInput.addEventListener('input', function () {
    updateButton.removeAttribute('disabled');
});
