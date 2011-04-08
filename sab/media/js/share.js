function formatAmount(dollarAmount) {
    return '$' + Math.floor(dollarAmount);
}

function getFBDonateMessage() {
    return "I am donating " + formatAmount(dollarAmount) + " to " +
        "the Elizabeth Taylor AIDS Foundation for every hour " +
        "Westboro spends protesting.";
}

function getFBSiteMessage() {
    return "We have received pledges to donate " + 
        formatAmount(TOTAL_AMOUNT) + " for every hour Westboro spends " +
        "protesting. The goal is " + formatAmount(TOTAL_AMOUNT_GOAL) + 
        ". Help out!";
}

function facebookURL(message) {
    var description = "Help us turn Westboro's protest of Liz Taylor's public memorial into a fundraising bonanza for the Elizabeth Taylor AIDS Foundation.";
    return 'http://www.facebook.com/dialog/feed' +
        '?app_id=' + FACEBOOK_APP_ID + 
        '&link=' + encodeURIComponent('http://sponsorabigot.org') +
        '&picture=' + encodeURIComponent(FB_IMAGE) +
        '&display=popup' +
        '&message=' + encodeURIComponent(message) +
        '&description=' + encodeURIComponent(description) +
        '&redirect_uri=' + encodeURIComponent(POPUP_REDIRECT_URL);
}

function openFacebook(message) {
    window.open(
        facebookURL(message),
        'post_to_fb', 'status=0,width=580,height=400');
}

function getTWDonateMessage() {
    return "Donating " + formatAmount(dollarAmount) + 
        " to Elizabeth Taylor AIDS Foundation for every hour Westboro protests Liz's funeral #sponsorabigot";
}

function getTWSiteMessage() {
    return "Donate to Elizabeth Taylor AIDS Foundation for every hour Westboro protests Liz's funeral. #sponsorabigot #greatidea";
}

function openTwitter(msg) {
    var url = "http://twitter.com/share?text=" + encodeURIComponent(msg) +
        "&url=" + encodeURIComponent('http://sponsorabigot.org');
    window.open(
        url,
        'post_to_tw', 'status=0,width=580,height=400');
}

$(function() {
    $('a.fb-sharedonation').click(function(e) {
        e.preventDefault();
        openFacebook(getFBDonateMessage());
    });
    $('a.fb-sharesite').click(function(e) {
        e.preventDefault();
        openFacebook(getFBSiteMessage());
    });    
    $('a.tw-sharedonation').click(function(e) {
        e.preventDefault();
        openTwitter(getTWDonateMessage());
    });
    $('a.tw-sharesite').click(function(e) {
        e.preventDefault();
        openTwitter(getTWSiteMessage());
    });
});