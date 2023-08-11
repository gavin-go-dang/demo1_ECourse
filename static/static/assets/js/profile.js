$('input[name="full_name"]').on('input', function () {
    $("#submit-btn").removeAttr('disabled');
});


$('input[name="username"]').on('input', function () {
    $("#submit-btn").removeAttr('disabled');
});

$('input[name="email"]').on('click', function () {
    $("#submit-btn").removeAttr('disabled');
});

function changing_check() {
    $("#submit-btn").removeAttr('disabled');
}

function check_date_change(e) {
    $("#submit-btn").removeAttr('disabled');
}

$('#button').click(function () {
    $("input[type='file']").trigger('click');
})
