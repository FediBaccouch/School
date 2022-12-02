function resultatBtn() {

    res = 0;

    if (document.getElementById("q1vrai").checked) {
        res += Number(document.getElementById("q1vrai").value);
    }
    if (document.getElementById("q2H").checked) {
        res += Number(document.getElementById("q2H").value);
    }
    if (document.getElementById("q3faux").checked) {
        res += Number(document.getElementById("q3faux").value);
    }

    alert("Votre score est: " + res);

}