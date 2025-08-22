let fruits = ["Apple", "Banana", "Cherry", "Pomegranate"];

let cars = new Array("Honda", "KIA", "Hyundai", "Range Rover");
console.log(cars);
//nambah new array

fruits = ["Apple", "Banana", "Cherry", "Pomegranate"];
// urutan    0      1      2          3
console.log(fruits[3]);
//akan menampilkan "Promegranate"

let fruit = ["Apple", "Banana", "Cherry", "Pomegranate"];
fruits[2] = "Mango";
console.log(fruits[2]);
//mengganti item, jd cherry akan diganti jd mango

//METHOD DI ARRAY

let poke = new Array("Alolan Raichu", "Talonflame", "Lapras");
poke.length;
//mengetahui bnyk item di list

let mcyt = new Array("Fundy", "Purpled", "Niki Nihachu");
mcyt.pop();
console.log(mcyt);
//menghapus item plg terakhir

let pokemon = ["Slyveon", "Umbreon", "Leafage", "Eeve"];
pokemon.push("Zoroark");
console.log(pokemon);

let mcyts = ["Techno", "Philza", "Sapnap", "BadBoyHalo"];
mcyts.shift();
console.log(mcyts);
//menghapus item plg awal

let Lmanburg = ["Tommyinnit", "Wilbur", "Ranboo", "Tubbo"];
Lmanburg.unshift(Jschlatt);
console.log(Lmanburg);
//menambahkan item baru di plg awal

let pogtopia = ["Dream", "George", "Sapnap", "Eret"];
pogtopia.slice(0,3);
//mengambil sebagian item
//Array ["George", "Sapnap"]



