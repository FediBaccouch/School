//fonction qui permet de vérifier si un chaine contient que des caractère dans l'intervalle [deb,fin]
function test(ch, deb, fin) {
  var i = -1;
  do {
    i = i + 1;
     } 
  while (i < ch.length - 1 && ch.charAt(i) >= deb && ch.charAt(i) <= fin);
  
  return ch.charAt(i) >= deb && ch.charAt(i) <= fin;
}
// à compléter...
function Verif1() {
  civilite = document.form.civilite;
  nom = document.getElementById("nom").value;
  gouverIndex = document.getElementById("gouver").selectedIndex;
  gouver = document.getElementById("gouver")[gouverIndex].value;
  interet = document.form.interet;

  if (!civilite[0].checked && !civilite[1].checked && !civilite[2].checked) {
    alert("Selectioner votre civilite!");
    return false;
  } else if (nom.length < 3 || nom.length > 20 || !test(nom.toUpperCase(), "A", "Z") || !test(nom[0], "A", "Z")) {
    alert("nom doit etre compose uniquement par des lettres alphabetiques entre 3 et 20 et commence par un lettre Majuscule!");
    return false;
  } else if (gouver != "Tunis" && gouver != "Sfax" && gouver != "Gabes") {
    alert("Selectionner votre gouvernorat!");
    return false;
  } else if (!interet[0].checked && !interet[1].checked) {
    alert("Selectionner un centre d'interet!");
    return false;
  }
  return true;
}