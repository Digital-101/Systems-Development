// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
});

// Load Theme from Local Storage
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
    }
});

// Form Validation and Calculator
const form = document.getElementById('insuranceForm');
const quoteResult = document.getElementById('quoteResult');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const carValue = parseFloat(document.getElementById('carValue').value);
    const driverAge = parseInt(document.getElementById('driverAge').value);
    const quote = (carValue * 0.05) - (driverAge > 25 ? 200 : 0);
    quoteResult.innerHTML = `Your estimated insurance quote is: R${quote.toFixed(2)}`;
});

// Slideshow Functionality
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

document.getElementById('nextSlide').addEventListener('click', () => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
});

document.getElementById('prevSlide').addEventListener('click', () => {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    slides[currentSlide].classList.add('active');
});

// Testimonial Functionality with Persistent Storage
const reviewsDiv = document.getElementById('reviews');

// Load reviews from local storage
const savedReviews = JSON.parse(localStorage.getItem('reviews')) || [];
savedReviews.forEach(review => addReviewToDOM(review));

document.getElementById('addReview').addEventListener('click', () => {
    const reviewInput = document.getElementById('reviewInput');
    const reviewText = reviewInput.value;
    if (reviewText) {
        addReviewToDOM(reviewText);
        savedReviews.push(reviewText);
        localStorage.setItem('reviews', JSON.stringify(savedReviews));
        reviewInput.value = '';
    }
});

function addReviewToDOM(reviewText) {
    const reviewElement = document.createElement('div');
    reviewElement.textContent = reviewText;
    reviewsDiv.appendChild(reviewElement);
}

// Chatbot Functionality with Basic Responses
const chatWindow = document.getElementById('chatWindow');
document.getElementById('sendChat').addEventListener('click', () => {
    const chatInput = document.getElementById('chatInput');
    const userMessage = chatInput.value;
    if (userMessage) {
        addChatMessage('You', userMessage);
        chatInput.value = '';
        // Simulated bot response
        const botResponse = getBotResponse(userMessage);
        addChatMessage('Bot', botResponse);
    }
});

function addChatMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    chatWindow.appendChild(messageElement);
}

function getBotResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    if (lowerMessage.includes('quote')) {
        return "I can help you with that! Please fill out the insurance form.";
    } else if (lowerMessage.includes('benefit')) {
        return "Our insurance provides many benefits including coverage for theft and accidents.";
    } else {
        return "I'm here to help! Please ask your question.";
    }
}
