function verif() {
    nom = document.getElementById("nom").value;
    prenom = document.getElementById("prenom").value;
    telephone = document.getElementById("telephone").value;
    email = document.getElementById("email").value;

    if(nom == "") {
    alert("Nom ne doit pas etre vide");
    return false;
    } else if(nom.length < 5) {
        alert("Nom doit etre au minimum 5 caracteres");
        return false;
    } else if(prenom == "") {
        alert("Prenom ne doit pas etre vide");
        return false;
    } else if(prenom.length < 5) {
        alert("Prenom doit etre au minimum 5 caracteres");
        return false;
    } else if(telephone == "") {
        alert("Telephone ne doit pas etre vide")
        return false;
    } else if(isNaN(telephone)) {
        alert("Telephone doit etre seulement des nombres")
        return false;
    } else if(telephone.length < 8) {
        alert("Telephone doit etre au minimum 8 nombres");
        return false;
    } else if(email.length < 10) {
        alert("Email doit etre au minimum 10 caracteres");
        return false;
    } else if(email.indexOf("@") > email.indexOf(".")) {
        alert("Email Invalide");
        return false;
    } else if(document.getElementById("html").checked == false && document.getElementById("css").checked == false && document.getElementById("js").checked == false && document.getElementById("php").checked == false) {
        alert("Selectioner un case");
        return false;
    }

    alert("Submited");
    return true;
}