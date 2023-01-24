function NombreDeMots() {
    ch = document.getElementById("texte").value;
    Nb = 0;
    
    for(i = 0; i < ch.length; i++) {
        if(ch[i] == " ") {
            Nb += 1;
        }
    }
    
    document.getElementById("NbMots").value = Nb + 1;
}

function NombreDeCaracteres() {
    ch = document.getElementById("texte").value;
    document.getElementById("NbCara").value = ch.length;
}

function NombreOccurence() {
    ch = document.getElementById("texte").value;
    c = document.getElementById("CaraRech").value;
    Nb = 0;

    if(c != "") {
        for(i = 0; i < ch.length; i++) {
            if(ch[i] == c) {
                Nb += 1;
            }
        }
        
        document.getElementById("NbOccu").value = Nb;
    }
}

function Annuler1() {
    document.getElementById("NbMots").value = "";
    document.getElementById("NbCara").value = "";
}

function Annuler2() {
    document.getElementById("CaraRech").value = "";
    document.getElementById("NbOccu").value = "";
}

function Comtage1() {
    NombreDeMots();
    NombreDeCaracteres();
}

function Comtage2() {
    NombreOccurence();
}