for ( let num = 0; num < 10; num++){
    console.log("Number" + num);
}

let trainer = {name : "Cygnet", class : "Veteran", age : "-" };

for (let num in trainer) {
    console.log(kunci + "+ " + trainer[num])
}

let pokemon = ["Talonflame", "Mimikyu", "Decidueye", "Leafeon"]

for ( let poke of pokemon) {
    console.log("I like " + poke);
}

number = 0;

while (number < 10) {
    console.log( "Number" + number);
    number++;
}

number = 0;

do{
    console.log("Number" + number);
    number++;
}

while(number < 10);

//plus dua maksudnya perputaran lbh dr sekali

//for-mengulang dgn jumlah pasti
//for in-mengambil nama properti di objek
//for of-mengambil isi di array atau string
//while-mengulang selama kondisinya benar
//do while-minimal sekali jalan, baru cek kondisi

//misalkan mau pembayaran kasir-pakai js trs statement yg dipakai-while
//cek data klo mau tau apa data udh ke isi bisa pakai-for in
//bikin sistem sign up, input pass pake -do while