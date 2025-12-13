$('#auth-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        const CSRF = $('[name=csrfmiddlewaretoken]').val();

        if(!email) {
            alert('Введите адрес электронной почты!');
        }

        if(!password) {
            alert('Ввеедите пароль!');
        }

        let userData = {
            'email' : email,
            'password' : password,
            'csrfmiddlewaretoken': CSRF
        }

        $.ajax({
            url: '/auth/',
            type: 'POST',
            dataType: 'json',
            data:  userData
        });
    }
);
