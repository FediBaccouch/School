function verif() {
    nom = f.nom.value;
    prenom = f.prenom.value;
    date = new Date(f.date.value);
    datedejour = new Date();

    if(nom == "") {
        alert("nom ne doit pas etre vide!");
        return false;
    } else if(prenom == "") {
        alert("prenom ne doit pas etre vide!");
        return false;
    } else if(isNaN(date)) {
        alert("choisissez une date de naissance!");
        return false;
    } else if(datedejour.getFullYear() - date.getFullYear() < 15 || datedejour.getFullYear() - date.getFullYear() > 50) {
        alert("Votre age doit etre entre 15 et 50!");
        return false;
    }

    return true;
}