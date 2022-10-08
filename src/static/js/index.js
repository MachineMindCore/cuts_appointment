const regis = document.querySelector('#register')
const login = document.querySelector('#login')

if (regis) regis.addEventListener('click', goRegister);
if (login) login.addEventListener('click', goLogin);

function goRegister() {
    location.href = '/registro'
}

function goLogin() {
    location.href = '/login'
}
