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
    var description = "Help us turn Westboro's protest of Liz Taylor's public memorial into a fundraising bonanza for the Elizabeth Taylor AIDS Foundation.";
    return 'http://www.facebook.com/dialog/feed' +
        '?app_id=' + FACEBOOK_APP_ID + 
        '&link=' + encodeURIComponent('http://sponsorabigot.org') +
        '&picture=' + encodeURIComponent(FB_IMAGE) +
        '&display=popup' +
        '&message=' + encodeURIComponent(getMessage(dollarAmount)) +
        '&description=' + encodeURIComponent(description) +
        '&redirect_uri=' + encodeURIComponent(POPUP_REDIRECT_URL);
}

function openFacebook() {
    window.open(
        facebookURL(dollarAmount),
        'post_to_fb', 'status=0,width=580,height=400');
}

function openTwitter() {
    var msg = "Donating " + formatAmount(dollarAmount) + 
        " to Elizabeth Taylor AIDS Foundation for every hour Westboro protests Liz's funeral #sponsorabigot";
    var url = "http://twitter.com/share?text=" + encodeURIComponent(msg) +
        "&url=" + encodeURIComponent('http://sponsorabigot.org');
    window.open(
        url,
        'post_to_tw', 'status=0,width=580,height=400');
}

$(function() {
    $('a.fb').click(function(e) {
        e.preventDefault();
        openFacebook();
    });
    $('a.twitter').click(function(e) {
        e.preventDefault();
        openTwitter();
    });
});