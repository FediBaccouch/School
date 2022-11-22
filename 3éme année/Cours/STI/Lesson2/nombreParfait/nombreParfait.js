for (i = 2; i < 1000; i++) {
    S = 0;
    for (j = 1; j <= Math.floor(i / 2); j++) {
        if ((i % j) == 0) {
            S += j;
        }
    }
    if (S == i) {
        document.write("<p>" + S + " est un nombre parfait</p>");
    }
}