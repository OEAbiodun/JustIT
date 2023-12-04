let coffeeOrder = [
    "James - Americano",
    "Jillian - Cappuccino",
    "Erica - Mocha"
]

console.log(coffeeOrder);
console.log(coffeeOrder.length);
console.log(coffeeOrder[0]);
console.log(coffeeOrder[1]);
console.log(coffeeOrder[2]);
console.table(coffeeOrder);


// Updating array list
// coffeeOrder[1] = "Hannah - Tea";
// console.log(coffeeOrder);

// coffeeOrder[2] = "Sarah - Cappucinno";
// console.log(coffeeOrder);

// Array Methods

coffeeOrder.pop() //Removes from the array
console.log(coffeeOrder);

coffeeOrder.push("Christian - Water") //Push into the array
console.log(coffeeOrder);
console.table(coffeeOrder);

let colours = [
    "Blue",
    "Red",
    "Green",
    "Yellow",
    "Indigo",
    "Purple"
];

// console.log(colours);
// console.log(colours[0])
// console.log(colours[1])
// console.log(colours[2])
// console.log(colours[3])
// console.log(colours[4])
// console.log(colours[5])

// Loop

// let a = 1;
// console.log(a);

// let b = a++;
// console.log(b)
// console.log(a)

// let c = ++a;
// console.log(c)

// For loop

// for (let i = 0; i < 5; i++) {
//     console.log(`Index value is currently ${i}`)
// }

// for (let i = 0; i < colours.length; i++) {
//     console.log(colours[i])
//     // console.table(colours[i])
// }

// while loop

let number = 0;

while (number < 10) {
    console.log(number)
    number++
}

let cards = ["Diamond", "Heart", "Club", "Spade"];
let currentCard = "";

while (currentCard !== "Spade") {
    currentCard = cards [Math.floor(Math.random() * 4)];
    console.log("!!!GAME OVER!!!")
}

let num = 10;

do{
    console.log(num)
}while (num < 1)

for (let i = 1; i <= 5; i++) {
    if (i === 3) {
        break
    }
    console.log(i);
}

const weekdays = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

for (let item of weekdays) {
    console.log(weekdays)
}

let string = "Hello";

for (let character of string) {
    console.log(character)
}