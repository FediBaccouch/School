function premier() {
  a = Number(document.getElementById("a").value);
  b = Number(document.getElementById("b").value);

  if (a <= 1 || b >= 1001 || a > b) {
    alert("Invalide")
    return false;
  } else {
    var ch = "";
    for (let i = a; i < b; i++) {
      if (checkPremier(i)) {
        ch += i + "   ";
      }
    }
    alert(ch)
    return true;
  }
}

function checkPremier(N) {
  var S = 0
  for (let i = 1; i < N + 1; i++) {
    if (N % i == 0) {
      S++;
    }
  }
  return S == 2;
}