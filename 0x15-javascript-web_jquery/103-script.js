$(document).ready(function() {
    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
            $('DIV#hello').text(data.hello);
        });
    }

    $('INPUT#btn_translate').click(fetchTranslation);

    $('INPUT#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });
});
