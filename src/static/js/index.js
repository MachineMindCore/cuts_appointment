const regis = document.querySelector('#register')
const login = document.querySelector('#login')

if (regis) regis.addEventListener('click', goRegister);
if (login) login.addEventListener('click', goLogin);

function goRegister() {
    location.href = 'http://192.168.1.118:5000/registro'
}

function goLogin() {
    location.href = 'http://192.168.1.118:5000/login'
}
