// Function without argument -->
// Membuat Function
 function greet(){
    console.log("Helooo, how your life?")
}

// Memanggil Function
greet()


// Function with parameter/argument -->
 function greet(name){
    alert("Heloo, how your life?" + name + "?")
 }

 let yourName = prompt("What's your name :D?")

 // Memanggil functiom diikuti parameter
 greet(yourName);

 // Function-Return (hny mghslkn nilai, tidak menampilkan apa-apa) -->
 function add(a, b){
    result = a + b;
    result_text = a + " + " + b + " = " + result;

    return result_text;
 }

 console.log(add(10, 11))

 // Function in Variable (kyk return juga tpi ada variable tmbhn jd bisa di output) -->
 function add(a,b){
    result = a + b;
    result_text = a + " + " + b + " = " + result;

    return result_text;
 }

 addition = add(10, 11);

 console.log("The result is" + addition);