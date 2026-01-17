$('#logout-link').click(
    function() {
        const CSRF = $('[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url: '/logout/',
            type: 'POST',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': CSRF
            },

            success: 
                function(data) {
                    window.location.href = '/'; //Переход на главную сайта
                },
        });
    }
);