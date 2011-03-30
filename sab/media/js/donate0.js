jQuery(function($) {
    $('#pledge_form').ajaxForm({
        dataType: 'json',
        success: function(data, status, xhr, $form) {
            if (data.success){
                $form.resetForm();
                $form.parent().hide().next().fadeIn();
            } else {
                $('div.errorlist', $form).empty();
                for (key in data.errors) {
                    var div = $('#' + key + '_errors');
                    var ul = $('<ul/>');
                    div.append(ul);
                    ul.html(['<li>', data.errors[key], '</li>'].join(''));
                    ul.fadeIn();
                }
                $('#submit_label').text('Submit');
            }
        },
        beforeSubmit: function(formData, $form, options) {
            $('#submit_label').text('Submitting...');
        }
    });
});
