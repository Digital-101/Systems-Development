const myDiv = document.getElementById('java');
const myButton = document.getElementById('css');

function changeColor(event) {
    myDiv.style.backgroundColor = "red";
    myDiv.textContent = "Hello World";

}
myDiv.addEventListener('click', changeColor);
myButton.addEventListener('click', changeColor);

function changeColour(event) {
    myDiv.style.backgroundColor = "green";
    myDiv.textContent = "Hello Wandi";

}
myDiv.addEventListener('mouseover', changeColour);
myButton.addEventListener('mouseover', changeColour);

function changeColours(event) {
    myDiv.style.backgroundColor = "blue";
    myDiv.textContent = "Hello Jongo";

}
myDiv.addEventListener('mouseout', changeColours);
myButton.addEventListener('mouseout', changeColours);

