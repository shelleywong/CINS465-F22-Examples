/*
  file: scripts/main.js
  author: Shelley Wong
  date: Aug 30, 2022
*/

// Write to an HTML element
const myHeading = document.querySelector('h1');
let myVar = 'Shelley Wong';
myHeading.textContent = 'Hello ' + myVar;

document.getElementById('cins465name').innerHTML = "CINS465 Fall 2022";

// Event handler example -- toggle between images
let myImage = document.querySelector('.myimages');
myImage.onclick = function(){
  let mySrc = myImage.getAttribute('src');
  if(mySrc == 'images/cows.jpeg'){
    myImage.setAttribute('src', 'images/cow-gettyimages.jpeg');
  }
  else{
    myImage.setAttribute('src', 'images/cows.jpeg');
  }
}

// button onclick example
const countdiv = document.querySelector('#countdiv');
let count = 0;
let mycounter = document.querySelector('#counter');
mycounter.onclick = function(){
  count++;
  countdiv.textContent = count;
}
