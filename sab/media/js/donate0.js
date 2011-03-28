jQuery(function($) {
    $('#pledge_form').ajaxForm({
        dataType: 'json',
        success: function(data, status, xhr, $form) {
            if (data.success){
                $form.resetForm();
                $form.parent().hide().next().fadeIn();
            } else {
                for (key in data.errors) {
                    var ul = $('#' + key + '_errors');
                    ul.html(['<li>', data.errors[key], '</li>'].join(''));
                    ul.fadeIn();
                }
                $('#submit_label').text('Submit');
            }
        },
        beforeSubmit: function(formData, $form, options) {
            $('ul.errorlist', $form).hide();
            $('#submit_label').text('Submitting...');
        }
    });
});
