function Verif() {
  nom = document.getElementById("nom").value;
  pre = document.getElementById("pre").value;
  nais = new Date(document.getElementById("nais").value);
  currentDate = new Date();
  age = currentDate.getFullYear() - nais.getFullYear();
  email = document.getElementById("email").value;
  tel = document.getElementById("tel").value;
  dip = document.getElementById("dip").selectedIndex;
  q2 = form.q2;
  q3 = form.q3;

  if (nom == "" || !alpha(nom)) {
    alert("nom invalide!");
    return false;
  } else if (pre == "" || !alpha(pre)) {
    alert("prenom invalide!");
    return false;
  } else if (isNaN(nais.getDay()) || age < 10 || age > 60) {
    alert("age invalide!");
    return false;
  } else if (
    email == "" ||
    email.indexOf("@") == -1 ||
    email.indexOf(".") == -1 ||
    email.indexOf("@") > email.indexOf(".")
  ) {
    alert("email invalide!");
    return false;
  } else if (tel.length != 8 || isNaN(tel)) {
    alert("telephone invalide!");
    return false;
  } else if (!q2[0].checked && !q2[1].checked && !q2[2].checked) {
    alert("Selectionner votre languages!");
    return false;
  } else if (!q3[0].checked && !q3[1].checked) {
    alert("Selectionner oui ou non!");
    return false;
  }

  alert("All good, thank you for sharing your info!!!");
  return true;
}

function alpha(ch) {
  ch = ch.toUpperCase();
  test = true;
  i = 0;
  while (i < ch.length && test) {
    if (ch[i] < "A" || ch[i] > "Z") {
      test = false;
    }
    i++;
  }
  return test;
}
