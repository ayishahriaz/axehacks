let currentIndex = 0; // Define currentIndex outside of the function

function moveCarousel(direction) {
    const carouselInner = document.querySelector('.carousel-inner');
    const carouselItems = document.querySelectorAll('.textbook-info');
    const totalItems = carouselItems.length;
    
    // Update currentIndex based on the direction
    currentIndex = (currentIndex + direction + totalItems) % totalItems;
    
    // Calculate offset to move the carousel
    const offset = -currentIndex * 100; // 100% per slide
    carouselInner.style.transform = `translateX(${offset}%)`;
}


let currentIndexLaptop = 0; // Define currentIndexLaptop outside of the function

function moveCarouselLaptop(direction) {
    const carouselInnerLaptop = document.querySelector('.laptop-carousel-inner');
    const carouselItemsLaptop = document.querySelectorAll('.laptop-info');
    const totalItemsLaptop = carouselItemsLaptop.length;
    
    // Update currentIndexLaptop based on the direction
    currentIndexLaptop = (currentIndexLaptop + direction + totalItemsLaptop) % totalItemsLaptop;
    
    // Calculate offset to move the carousel
    const offsetLaptop = -currentIndexLaptop * 100; // 100% per slide
    carouselInnerLaptop.style.transform = `translateX(${offsetLaptop}%)`;
}
