number = prompt("Masukkan angka");

if (number % 2 == 0) {
    alert("Angka " + number + " adalah genap");
}

number = prompt("Masukkan angka");

if (number % 2 == 0) {
    alert("Angka " + number + " adalah genap");
} else {
    alert("Angka " + number + " adalah ganjil");
}

harini = prompt("Bagaimana cuaca hari ini?");

if (harini == "dingin") {
    alert("Tetap pakai sunscreen ya! Sinar matahari tetap mengintai kita");
} else if (harini == "panas") {
    alert("Harus pakai sunscreen! Agar kulit kita tercegah dari flek dini");
} else {
    alert("Selalu pakai sunscreen! Demi menjaga kulit sehat kita!")
}

number = prompt ("Masukkan angka");

mod = number % 2;

switch (mod) {
    case 0:
        alert(number + " adalah angka genap");
        break;
    case 1: 
        alert(number + " adalah angka ganjil");
        break;
      default:
        alert("hanya menerima angka");
        break;
}

