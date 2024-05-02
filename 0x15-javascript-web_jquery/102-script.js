$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        const languageCode = $('#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
