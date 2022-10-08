const regis = document.querySelector('#register')
const login = document.querySelector('#login')
const out = document.querySelector('#out')
const reserva = document.querySelector('#reserva')

if (regis) regis.addEventListener('click', goRegister);
if (login) login.addEventListener('click', goLogin);
if (out)  out.addEventListener('click', goOut)
if(reserva) reserva.addEventListener('click', goDash)


function goRegister() {
    location.href = '/registro'
}

function goLogin() {
    location.href = '/login'
}

function goOut() {
    location.href = '/logout'
}

function goDash() {
    location.href = '/dash'
}