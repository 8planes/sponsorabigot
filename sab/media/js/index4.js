$(function() {
    var counter = 1;

    var next = function() {
        counter++;
        $('.bigpoint-content').fadeOut(1000);
        var hourDiv = $('<p/>').addClass('bigpoint bigpoint-content').text(counter + ' hours?').hide();
        var dollarDiv = $('<p/>').addClass('bigpoint bigpoint-content').text('$' + (counter * 1243)).hide();
        $('#hours').append(hourDiv);
        $('#dollars').append(dollarDiv);
        hourDiv.fadeIn(1000);
        dollarDiv.fadeIn(1000);
        if (counter < 3)
            window.setTimeout(next, 3000);
    };

    window.setTimeout(next, 3000);
});