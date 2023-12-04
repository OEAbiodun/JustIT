let film = [
    "Knight", 
    "Mission Impossible", 
    "Welcome To America", 
    "Planet of the Ape", 
    "Star Gazer"];

    console.log(film);

    film.push("Titans", "Fly");
    console.log(film);

    for (let i = 0; i < film.length; i++) {
        console.log(`${film}`);
        // console.log(`${i}`);
    }

// Assignment 2
let num = [];
while (num.length < 10) {
     let numb = [Math.floor(Math.random() * 100) + 1];
    if(num.indexOf(numb) === -1) num.push(numb);
}
console.log(num);

// Assignment 3

let count;
for (count = 20; count >= 0; count--){
    console.log(count);
}