$(document).ready(function () {
  console.log('start')
  // Lấy các phần tử form
  const form = $('#registrationForm');
  const usernameInput = $('#username');
  const fullNameInput = $('#full_name');
  const emailInput = $('#email');
  const passwordInput = $('#password');
  const confirmPasswordInput = $('#confirm_password');
  const submitButton = $('#btnSubmit');

  // Thêm sự kiện nghe khi người dùng nhập dữ liệu
  form.on('input', function () {
    // Kiểm tra điều kiện và kiểm tra mật khẩu
    console.log('check')
    if (
      usernameInput.val() !== '' &&
      fullNameInput.val() !== '' &&
      emailInput.val() !== '' &&
      passwordInput.val() !== '' &&
      confirmPasswordInput.val() !== '' &&
      passwordInput.val() === confirmPasswordInput.val()
    ) {
      console.log('OK')
      submitButton.prop('disabled', false); 
      $('#input-submit').css('background-color', 'blue');
    } else {
      console.log('not ok')
      submitButton.prop('disabled', true); 
      $('#input-submit').css('background-color', '#d58cff');
    }
  });
});