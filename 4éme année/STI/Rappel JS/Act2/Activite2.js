function parfaits() {
  var ch = ""
  for (let i = 2; i < 1000; i++) {
    if (checkParfait(i)) {
      ch += i + "   ";
    }
  }
  alert(ch)
}

function checkParfait(N) {
  var S = 0;
  for (let i = 1; i < N; i++) {
    if (N % i == 0) {
      S += i;
    }
  }
  return S == N;
}