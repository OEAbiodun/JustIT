
const submit = document.getElementById('lik');
lik.addEventListener('click', thisFunc)

function thisFunc() {
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const random = fname[Math.floor(Math.random() * fname.length)] + lname[Math.floor(Math.random() * lname.length)];
    alert(random);
}

