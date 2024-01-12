function determinerJour() {
  M = Number(document.getElementById("month").value);
  A = Number(document.getElementById("year").value);

  if (M == 0 || A == 0) {
    alert("Donner Mois et Annee!");
    return false;
  } else {
    if (M == 1 || M == 3 || M == 5 || M == 7 || M == 8 || M == 10 || M == 12) {
      J = 31;
    } else if (M == 2) {
      if ((A % 4 == 0 && A % 100 != 0) || A % 400 == 0) {
        J = 29;
      } else {
        J = 28;
      }
    } else {
      J = 30;
    }

    alert("Nombre de jours = " + J);
    return true;
  }
}
