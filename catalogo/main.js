let slideIndex = 0;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let products = document.getElementsByClassName("product");
  let limit;
  let start;
  
  if (n > Math.floor(products.length/5)) {slideIndex = 0}
  if (n < 0) {slideIndex = Math.floor(products.length/5)}
  
  for (i = 0; i < products.length; i++) {
    products[i].style.display = "none";
  }

  slideIndex * 5 + 5 > products.length? start = products.length - 5: start = slideIndex * 5;
  slideIndex * 5 + 5 > products.length? limit = products.length : limit = slideIndex * 5 + 5;

  for (i = start; i < limit; i++) {
    products[i].style.display = "block";
  }
}