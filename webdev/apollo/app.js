const imgLinks = [
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/LungLife_banner_Web.jpg', 
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/Desktop.jpg', 
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/emergency_banner_web-674e9396b809b.jpg', 
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/proton_cancer_banner_web-674e93cac64aa.jpg', 
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/APH_New-Year_Ask-Apollo_1920x542_Apollo_desktop-.jpg', 
    'https://cdn.apollohospitals.com/dev-apollohospitals/2024/12/41Anniversary_banner_web-674e92be572f3.jpg'
];
const carousel = document.getElementById('carousel');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
let index = 0;

// Insert images into the carousel
imgLinks.forEach(link => {
    const imgDiv = document.createElement('div');
    imgDiv.className = 'w-full flex-shrink-0';
    const img = document.createElement('img');
    img.src = link;
    img.alt = 'Apollo Hospitals Banner';
    img.className = 'w-full h-full object-cover';
    imgDiv.appendChild(img);
    carousel.appendChild(imgDiv);
});

function showSlide(i) {
    const totalSlides = imgLinks.length;
    index = (i + totalSlides) % totalSlides;
    carousel.style.transform = `translateX(-${index * 100}%)`;
}

prevButton.addEventListener('click', () => showSlide(index - 1));
nextButton.addEventListener('click', () => showSlide(index + 1));