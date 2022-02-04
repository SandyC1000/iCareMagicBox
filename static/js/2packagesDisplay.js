"use strict";

console.log("Reached 2packages_display.js")

const carePackage = {
    "package_id": 1, 
    "package_type": "Energy"
    }


const button = document.querySelector('#next-packages');

function handleClick() {
  document.querySelector('#new-box').insertAdjacentHTML('afterbegin',"<img class='card-img-top img-circle' style='width: 320px; height: 320px;' src='/static/img/box_1.jpg'>");
}

button.addEventListener('click', handleClick);

