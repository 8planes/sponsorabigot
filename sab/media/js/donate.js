(function() {
    var email = ["inf", "o", "@spo", "nsorabigot.org"].join('');
    var elem = document.getElementById('our_email');
    elem.href = "mailto:" + email;
    elem.innerHTML = email;
})();