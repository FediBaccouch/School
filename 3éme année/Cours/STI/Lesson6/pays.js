function selectBtn() {
    choix = document.getElementById("pays").selectedIndex;
    pay = document.getElementById("pays").options[choix].value;
    
    alert("Je suis " + pay)
}