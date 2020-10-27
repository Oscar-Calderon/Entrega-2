function validarContras(){
    var pass1 = document.getElementById('pw1').value;
    var pass2 = document.getElementById('pw2').value;

    if(pass1 != pass2){
        alert("Las contraseñas ingresadas no son iguales.");
        return false;
    }
}

function validaRut(rut) {
    var numero = rut.value.replace('.','');
    numero = numero.replace('-','');
    rutN = numero.slice(0,-1);
    dv = numero.slice(-1).toUpperCase();
    rut.value = rutN + '-'+ dv

    if(rutN.length < 7 || rutN.length > 8) {
        rut.setCustomValidity("Formato Erroneo");
        return false;
    }

    else{
        rut.setCustomValidity('');
    }
}

function galleta() {
  alert("¡La galleta de la fortuna dice que tendrás un buen dia!");
}

function construccion(){
    alert("Sitio En Construcción, Todavía no disponible!");
}

function nodisp(){
    alert("Función todavía no disponible!");
}

var count = 0;
var countIn = document.getElementById("itemsa")

function agregar(){
    count++;
    countIn.value = count;
}
