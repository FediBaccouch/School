function addition() {
    a = Number(prompt("donner a: "));
    b = Number(prompt("donner b: "));
    alert(a + " + " + b + " = " + (a + b));
}

function subtraction() {
    a = Number(prompt("donner a: "));
    b = Number(prompt("donner b: "));
    alert(a +" - " + b + " = " + (a - b));
}

function division() {
    a = Number(prompt("donner a: "));
    b = Number(prompt("donner b: "));
    if (b != 0) {
        alert(a +" / " + b + " = " + (a / b));
    } else {
        alert("division impossible par 0!")
    }
    
}

function multiplication() {
    a = Number(prompt("donner a: "));
    b = Number(prompt("donner b: "));
    alert(a + " x " + b + " = " + (a * b));
}