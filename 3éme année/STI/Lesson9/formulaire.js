function Sent() {
    nomPrenom = document.getElementById("nomPrenom").value;
    email = document.getElementById("email").value;
    if(nomPrenom == "") {
        alert("Nom & Prenom doit etre non vide");
        return false;
    } else if(!alphabetique(nomPrenom)) {
        alert("Nom & Prenom doit etre alphabetique");
        return false;
    } else if(nomPrenom.length < 15) {
        alert("Le longeur de Nom & Prenom doit etre au minimum 15");
        return false;
    } else if(email == "") {
        alert("Email doit etre non vide");
        return false;
    } else if(email.indexOf("@") > email.indexOf(".") || email.indexOf("@") == -1 || email.indexOf(".") == -1) {
        alert("email invalide");
        return false;
    } else if(email.indexOf("@") < 10) {
        alert("Le longeur de nom dont le mail doit etre au minimum 10");
        return false;
    } else if(email.indexOf(".") - email.indexOf("@") - 1 < 5) {
        alert("Le longeur de domaine dont le mail doit etre au minimum 5");
        return false;
    } else if(email.length - email.indexOf(".") - 1 < 2 || email.length - email.indexOf(".") - 1 > 3) {
        alert("l'extension dont le mail doit etre entre 2 et 3");
        return false;
    } else if(!document.getElementById("homme").checked && !document.getElementById("femme").checked) {
        alert("Selectioner un genre");
        return false;
    } else if (!document.getElementById("Lec").checked && !document.getElementById("Spo").checked && !document.getElementById("Voy").checked && !document.getElementById("Jeu").checked) {
        alert("Selectioner un Laisir");
        return false;
    }

    alert("Submited")
    return true;
}

function alphabetique(ch) {
    ch.toLowerCase();
    ok = true
    i = 0
    while(i < ch.length && ok) {
        if(ch[i] < "a" || ch[i] > "z") {
            ok = false;
        }
        i++;
    }
    return ok;
}