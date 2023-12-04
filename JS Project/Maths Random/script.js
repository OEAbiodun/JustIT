const toggleBtn = document.querySelector('.darkbtn');
toggleBtn.addEventListener('click', () => {
document.documentElement.classList.toggle('dark-mode');
});

const operators = ['+','-','*','/'];
const soundbtn = document.querySelector('.sound');
//generate random numbers
let firstNumber = parseInt(Math.random()*10);
let secondNumber = parseInt(Math.random()*10);

op = operators[Math.floor(Math.random()*4)];
//get the total
let total = eval(firstNumber + op + secondNumber);

//This will display numbers on the canvas
let primary = document.getElementById('primaryNo');
    primary.innerHTML = `<p>${firstNumber}</p>`;

let se = document.getElementById('mult');
    se.innerHTML = `<p>${op}</p>`

let secondary = document.getElementById('secondaryNo');
    secondary.innerHTML = `<p>${secondNumber}</p>`



let button = document.getElementById('btn')

button.addEventListener('click', function(){

let guess = document.getElementById('guess').value;
    guess = Number(guess);

if (guess === total){
    alert(`Answer Is Correct. ${total}`);
    window.location.reload()
} else {
    alert('Sorry. Incorrect. The correct answer is ' + total + '.')
    window.location.reload()

}
});

soundbtn.addEventListener("click", ()=>{
    let utterance = new SpeechSynthesisUtterance(`${primaryNo.innerText} ${op} ${secondaryNo.innerText} equals ${total}`);
    speechSynthesis.speak(utterance);
})
