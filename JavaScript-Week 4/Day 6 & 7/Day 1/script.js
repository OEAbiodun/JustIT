const element = document.getElementById("header");
console.log(element);

const ele = document.getElementById("header").innerHTML = "JavaScript Dom";
console.log(ele);

// const elem = document.getElementsByClassName("main").innerHTML = "Text Changed";

const elem = document.getElementsByClassName("main")

const e = document.querySelector('.main').innerHTML = 'Text Changed';
console.log(e);

const li = document.getElementsByTagName('li');
for (let i=0;i<li.length;i++){
    li[i].style.color = 'Red';
}

const divh = document.createElement("h1");
const txt = document.createTextNode("This is new Div");
divh.appendChild(txt);
const st = document.getElementById("header-div");
st.appendChild(divh);


divh.style.fontSize = "60px";
divh.style.color = "orange";
divh.style.backgroundColor = "gray";

// const lik = document.getElementById('bg');
// lik.style.backgroundColor = "green";

function myFunction(){
    let elep = document.body;
    elep.classList.toggle("dark-mode");
}


const hide=document.getElementById('hide');
const paragraph = document.getElementById('p1');
hide.addEventListener('click', function hideMe(){
    // document.getElementById('p1').style.display='none';
    // alert("Button is clicked")
    if(paragraph.style.display=='none')
    {
        paragraph.style.display="block";
    }else{
        paragraph.style.display="none";
    }
})
// console.log(hide);

let greeting =()=>{
    alert("Hello, how are you");
}

const clickButton=document.getElementById('media');
clickButton.addEventListener('click', greeting)