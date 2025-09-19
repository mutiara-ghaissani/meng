let btn = document.getElementById("hitungbtn")
let result = document.getElementById("result")

btn.oneclick = function() {
    let berat = document.getElementById("Berat Badan").value;
    let tinggicm = document.getElementById("Tinggi").value;

    berat = parseFloat(berat)
    tinggicm = parseFloat(tinggicm)

    if (isNaN(berat) || isNaN(tinggicm) || berat <= 0 || tinggicm <= 0) {
        result.innerHTML = "MASUKKAN NILAI YANG VALID!";
        return;
    }

    let tinggiM = tinggicm
    let bmi = berat / (tinggiM * tinggiM);
    let kategori = "";

    if (bmi < 18.5) {
        kategori = "kurus";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        kategori = "normal";
    } else if (bmi >= 25 && bmi <= 29.9) {
        kategori = "kelebihan berat badan";
    } else {
        kategori = "obesitas";
    }

    result.innerHTML = "BMI kamu: " + bmi.toFixed(2) + "->" + kategori ;

}