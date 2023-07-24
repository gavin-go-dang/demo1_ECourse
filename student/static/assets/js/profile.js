
const fullNameInput = document.querySelector('input[name="full_name"]');

const usernameInput = document.querySelector('input[name="username"]');

const emailInput = document.querySelector('input[name="email"]');

const dateInput = document.querySelector('input[name="date"]');

const updateButton = document.querySelector('input[name="update"]');

fullNameInput.addEventListener('input', function () {
    updateButton.removeAttribute('disabled');
});

emailInput.addEventListener('input', function () {
    updateButton.removeAttribute('disabled');
});


updateButton.addEventListener('click', function () {
    usernameInput.removeAttribute('disabled');
});


function changing_check() {
    updateButton.removeAttribute('disabled');
}


function check_date_change(e) {
    updateButton.removeAttribute('disabled');
}

$('#button').click(function () {
    $("input[type='file']").trigger('click');
})
