var dollarAmount = 1;

jQuery(function($) {
    $('a.button').click(function(e) {
        e.preventDefault();
        $('#pledge_form').submit();
    });

    $('#pledge_form').ajaxForm({
        dataType: 'json',
        success: function(data, status, xhr, $form) {
            dollarAmount = parseFloat($('#id_amount').val());
            if (data.success){
                $form.resetForm();
                $form.parent().hide().next().fadeIn();
            } else {
                $('div.errormsg div').empty();
                for (key in data.errors) {
                    var div = $('#' + key + '_errors');
                    $('div', div).text(data.errors[key]);
                    div.fadeIn();
                }
                $('#submit_label').text('Submit');
            }
        },
        beforeSubmit: function(formData, $form, options) {
            $('#submit_label').text('Submitting...');
        }
    });
});
