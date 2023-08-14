$(document).ready(function () {
    $('input[type="radio"]').change(function () {
        let allAnswered = true;
        $('input[type="radio"]').each(function () {
            if (!$('input[name="' + $(this).attr('name') + '"]:checked').length) {
                allAnswered = false;
                return false;
            }
        });

        if (allAnswered) {
            $('button[type="submit"]').prop('disabled', false);
        } else {
            $('button[type="submit"]').prop('disabled', true);
        }
    });
});