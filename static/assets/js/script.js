$('#password, #confirm_password').on('keyup', function () {
  const password = $('#password').val();
  const confirm_password = $('#confirm_password').val();
  if (password === confirm_password && password !== '') {
    $('#message').html('Matching').css('color', 'green');
    $('#btnSubmit').prop('disabled', false);
  } else {
    $('#message').html('Not Matching').css('color', 'red');
    $('#btnSubmit').prop('disabled', true);
  }
});