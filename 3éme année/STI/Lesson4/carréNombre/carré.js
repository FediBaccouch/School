function carré() {
    num = document.getElementById("nombre").value;
    if (isNaN(num)) {
        document.getElementById("Output").value = "impossible";
    } else {
        document.getElementById("Output").value = num * num;
    }
}