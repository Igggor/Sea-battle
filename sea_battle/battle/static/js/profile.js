function admVis() {
    document.getElementById('passForm').style.display = "none";
    document.getElementById('nameForm').style.display = "none";
    document.getElementById('admForm').style.display = "block";
}
function nameVis() {
    document.getElementById('admForm').style.display = "none";
    document.getElementById('passForm').style.display = "none";
    document.getElementById('nameForm').style.display = "block";
}
function passVis() {
    document.getElementById('nameForm').style.display = "none";
    document.getElementById('admForm').style.display = "none";
    document.getElementById('passForm').style.display = "block";
}