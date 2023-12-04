// localStorage.setItem('name', 'Olu')

// console.log(localStorage.getItem('name'))

// // To delete the data from localstorage
// localStorage.removeItem('name');

// console.log(localStorage.getItem('name'));

// //To completely clear local storage
// localStorage.clear();


const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
const submit = document.getElementById("submit");

submit.addEventListener('click', saveit)

function saveit(){
    localStorage.setItem('fname', fname.value);
    localStorage.setItem('lname', lname.value);
    console.log(localStorage.getItem('fname'))
    console.log(localStorage.getItem('lname'))
    document.getElementById('p2').innerText=`${fname.value} ${lname.value}`;
}

const date = new Date();
console.log(date);
document.getElementById('time').innerHTML = date;



// const number = (string, index, num) 
// function num() {
//     console.log(string.substr(index, num));
// }
// number("I'm not sure.", 3, 10);




const par1 = document.getElementById('par1');
const par2 = document.getElementById('par2');
const but = document.getElementById('but');

but.addEventListener('click', clickit)

function clickit() {
        document.getElementById('pot1').innerText=`${par1.value} ${par2.value}`;
        if (randomNumber < 0.5) {
    alert(par1);
}
// Otherwise, alert the second text box
else {
    but.addEventListener('click', clickit)
    alert(par2);
}
}

// const text1 = document.getElementById("par1").value;
// const text2 = document.getElementById("par2").value;

// // Generate a random number between 0 and 1
// const randomNumber = Math.random();

// // If the random number is less than 0.5, alert the first text box
// if (randomNumber < 0.5) {
//     alert(par1);
// }
// // Otherwise, alert the second text box
// else {
//     alert(par2);
// }