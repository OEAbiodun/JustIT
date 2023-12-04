let age = 18;

if (age >= 18){
    console.log('You are old enough to be served Alcohol.');
}
else if (age < 18){
    console.log("Sorry, you aren't old enough yet.");    
}

// Password string

let password = "Oluwaseun";

let len = password.length;


if (len >= 9){
    console.log(password);
}else if (len < 9) {
    console.log("Password is too short");    
}


let num = 14;

if (num % 3 === 0 || num % 5 ===0){
    console.log(`${num} can be divided by either 3 or 5`);    
}else {
    console.log("Number not divisible by 3 or 5")
}


let number = 21;

if (number % 3 === 0 && number % 5 === 0) {
    console.log("Fizz Buzz");
}else if (number % 5 === 0){
    console.log(` ${number} Buzz`);   
} else if (number % 3 === 0){
    console.log(`${number} Fizz`);
}else{
    console.log("Try again")
}

