$('input[name="full_name"]').on('input', function () {
    $updateButton.removeAttr('disabled');
});

$('input[name="username"]').on('input', function () {
    $updateButton.removeAttr('disabled');
});

$('input[name="email"]').on('click', function () {
    $usernameInput.removeAttr('disabled');
});

function changing_check() {
    $updateButton.removeAttr('disabled');
}

function check_date_change(e) {
    $updateButton.removeAttr('disabled');
}

$('#button').click(function () {
    $("input[type='file']").trigger('click');
})
