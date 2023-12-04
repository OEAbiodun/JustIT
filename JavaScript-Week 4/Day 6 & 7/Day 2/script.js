// const button = document.getElementById('btnClick');
// const text = document.getElementById('txtName');

// button.addEventListener('click', getValue)

// function getValue(){
//     // alert('How, are you doing ${text.value}?');
//     document.getElementById('p1').innerText=text.value;
// }



const ftxt = document.getElementById('fName');
const ltxt = document.getElementById('lName');
const button = document.getElementById('btn');

button.addEventListener('click', getValue)

function getValue(){
    // alert('How, are you doing ${text.value}?');
    document.getElementById('p2').innerText=`${fName.value} ${lName.value}`;
    // document.getElementById('p3').innerText=ltxt.value;
}


// Image swapping code
const swap = document.getElementById('btnswap');
swap.addEventListener('click', swapPictures) 

function swapPictures() {
    const firstPic = document.getElementById('firstPic').src;
    const secondPic = document.getElementById('secondPic').src;
    document.getElementById('firstPic').src=secondPic;
    document.getElementById('secondPic').src=firstPic;
}