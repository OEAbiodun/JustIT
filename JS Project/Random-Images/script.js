const toggleBtn = document.querySelector('.btn');
toggleBtn.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark-mode');
});

const imgContainer = document.querySelector(".div-container");

const btn = document.querySelector(".btn-down");

btn.addEventListener("click", () => {
  imageNumber = 8;
  addNewImages();
});

function addNewImages() {
  for (let index = 0; index < imageNumber; index++) {
    const randImg = document.createElement("img");
    randImg.src = `https://source.unsplash.com/random/=${Math.floor(
    Math.random() * 2000
    )}`
    imgContainer.appendChild(randImg);
  }
}
