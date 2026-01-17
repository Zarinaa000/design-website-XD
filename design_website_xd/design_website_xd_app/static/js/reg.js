$('#reg-button').click(
    function() {

        //Подбираем данные с HTML
        let email = $('#email').val();
        let password = $('#password').val();
        let birthdate = $('#birthdate').val();
        let firstName = $('#first-name').val();
        let lastName = $('#last-name').val();
        let regButton = $('#reg-button');

        const CSRF = $('[name=csrfmiddlewaretoken]').val();
        
        if(!email) {
            alert('Введите адрес электронной почты!');
        }

        if(!password) {
            alert('Введите пароль!');
        }

        let userData = {
            'email' : email,
            'password' : password,
            'birthdate' : birthdate,
            'firstName' : firstName,
            'lastName' : lastName,
            'csrfmiddlewaretoken': CSRF
        }

        $.ajax({
            url: '/reg/',
            type: 'POST',
            dataType: 'json',
            data: userData,

            success: 
                function(data) {
                    regButton.text('Успешно');
                    regButton.prop('disabled', true);
                    regButton.css({
                        'background-color': '#4CAF50',
                        'color': '#fff',
                    });
                    window.location.href = '/'; //Переход на главную сайта
                },
        });
    }
);