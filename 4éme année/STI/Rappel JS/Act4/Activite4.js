function ppcm() {
  M = Number(document.getElementById("M").value);
  N = Number(document.getElementById("N").value);

  if (M == 0 || N == 0) {
    alert("Donner M et N!")
    return false;
  } else {
    if (M > N) {
      Max = M;
      Min = N;
    } else {
      Max = N;
      Min = M;
    }
  
    while (Max % Min != 0) {
      Max = Max + (M + N - Min);
    }
    
    alert("PPCM(" + M + "," + N + ") = " + Max);
    return true
  }
}