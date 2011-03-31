function formatAmount(dollarAmount) {
    var cents = (Math.floor(dollarAmount * 100) % 100) + '';
    if (cents.length < 2)
        cents = '0' + cents;
    return '$' + Math.floor(dollarAmount) + "." + cents;
}

function getMessage(dollarAmount) {
    return "I am donating " + formatAmount(dollarAmount) + " to " +
        "the Elizabeth Taylor AIDS Foundation for every hour " +
        "Westboro spends protesting. http://goo.gl/XwDpl";
}

function facebookURL(dollarAmount) {
    // see http://developers.facebook.com/docs/reference/dialogs/feed/
    return 'http://www.facebook.com/dialog/feed' +
        '?app_id=' + FACEBOOK_APP_ID + 
        '&link=' + encodeURIComponent('http://sponsorabigot.org') +
        '&display=popup' +
        '&message=' + encodeURIComponent(getMessage(dollarAmount)) +
        '&redirect_uri=' + encodeURIComponent(POPUP_REDIRECT_URL);
}

function openFacebook() {
    window.open(
        facebookURL(dollarAmount),
        'post_to_fb', 'status=0,width=580,height=400');
}

$(function() {
    $('a.fb').click(function(e) {
        e.preventDefault();
        openFacebook();
    });
});