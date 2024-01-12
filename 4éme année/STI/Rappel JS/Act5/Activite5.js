function combinaison() {
  n = Number(document.getElementById("n").value);
  p = Number(document.getElementById("p").value);

  if (n < p || p < 0) {
    alert("Invalide");
    return false;
  } else {
    C = fact(n) / (fact(n - p) * fact(p));
    alert(C);
    return true;
  }
}

function fact(N) {
  F = 1;
  for (let i = 1; i < N + 1; i++) {
    F = F * i
  }
  return F;
}