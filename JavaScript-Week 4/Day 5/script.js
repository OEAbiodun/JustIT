console.log("Olu")

// Javascript Object

const person = {
    name: "John",
    age: "31"
}

//CoffeeShop Example

const  coffeeShop = {
    name: "Costa",
    branchNumber: 250,
    specialOffers: true,
    drinks: [
        "Americano",
        "Latte",
        "Mocha",
    ]
}
console.log(coffeeShop);
console.table(coffeeShop);
console.table(coffeeShop.name);
console.table(coffeeShop["branchNumber"]);
console.table(coffeeShop.drinks[0]);


// Adding items to an existing object

coffeeShop.muffins = ["Blueberry", "Chocolate"];
console.table(coffeeShop);

//Overwrite / Change data in an existing object

coffeeShop.branchNumber = 100;
console.table(coffeeShop)

coffeeShop.breakfastOffer = "Free Bagel with any Coffee!"
coffeeShop.lunchOffer = "Free coffee with any Sandwich!"

let offer = "No current offer!";
let time = 1300;

if (time < 1100) {
    offer = coffeeShop.breakfastOffer;
    console.log(offer)
}else if (time < 1500) {
    offer = coffeeShop.lunchOffer;
    console.log(offer)
}

coffeeShop.open = function() {
    return "We are open come in!"
}

console.log(coffeeShop.open())


coffeeShop.close = function() {
    return "We are open closed!"
}

console.log(coffeeShop.close())
console.log(coffeeShop)

//Alarm object

const alarm = {
    weekendAlarm: "Sleep in its the weekend",
    weekdayAlarm: "Get up at 7:00am",
    checkDay: function(day){
        if (day === "Saturday" || day === "Sunday"){
        return this.weekendAlarm
    }else {
        return this.weekdayAlarm
    }
    }
}

console.log(alarm.checkDay("Sunday"))