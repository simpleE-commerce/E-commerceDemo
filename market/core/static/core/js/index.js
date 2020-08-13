const items = document.querySelectorAll('.slider-img');
const itemCount = items.length;
const nextItem = document.querySelector('.next');
const previousItem = document.querySelector('.previous');
let count = 0;
var slideIndex = 0;


function showNextItem() {
  items[count].classList.remove('active');

  if(count < itemCount - 1) {
    count++;
    slideIndex++;
  } else {
    count = 0;
    slideIndex = 0;
  }

  items[count].classList.add('active');
//   console.log(count);

  showSlides();
}

function showPreviousItem() {
  items[count].classList.remove('active');

  if(count > 0) {
    count--;
    slideIndex--;
  } else {
    count = itemCount - 1;
    slideIndex = itemCount - 1;
  }

  items[count].classList.add('active');
//   console.log(count);
showSlides();
}

function keyPress(e) {
  e = e || window.event;
  
  if (e.keyCode == '37') {
    showPreviousItem();
  } else if (e.keyCode == '39') {
    showNextItem();
  }
}

nextItem.addEventListener('click', showNextItem);
previousItem.addEventListener('click', showPreviousItem);
document.addEventListener('keydown', keyPress);


function showSlides() {
  var i;
//   var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";  
//   }
  
//   if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
//   slides[slideIndex-1].style.display = "block";  
  dots[slideIndex].className += " active";
//   setTimeout(showSlides, 2000); // Change image every 2 seconds
console.log(slideIndex);
}