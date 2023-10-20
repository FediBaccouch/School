//fonction qui permet de vérifier si un chaine contient que des caractère dans l'intervalle [deb,fin]
function test(ch, deb, fin) {
  var i = -1;
  do {
    i = i + 1;
  } while (i < ch.length - 1 && ch.charAt(i) >= deb && ch.charAt(i) <= fin);
  return ch.charAt(i) >= deb && ch.charAt(i) <= fin;
}
// à compléter...

function Verif1() {
  cin = document.getElementById('cin').value;
  num = document.getElementById('num').value;

  if (cin.length != 8 || !test(cin, '0', '9') || cin[0] === '0') {
    alert("CIN invalide!");
    return false;
  } else if (num.length != 8 || !test(num, '0', '9') || num[0] === '0') {
    alert("Num invalide!");
    return false;
  }
  alert("Success!");
  return true;
}

function Verif2() {
  cin = document.getElementById('cin').value;
  num = document.getElementById('num').value;
  r1 = document.getElementById('r1').checked;
  r2 = document.getElementById('r2').checked;
  r3 = document.getElementById('r3').checked;
  r4 = document.getElementById('r4').checked;

  if (cin.length != 8 || !test(cin, '0', '9') || cin[0] === '0') {
    alert("CIN invalide!");
    return false;
  } else if (num.length != 8 || !test(num, '0', '9') || num[0] === '0') {
    alert("Num invalide!");
    return false;
  } else if (!r1 && !r2 && !r3 && !r4) {
    alert("Selectionner le nombre de points a transformer!")
    return false;
  }
  alert("Success!")
  return true;
}