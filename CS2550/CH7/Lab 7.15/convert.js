function convertCToF(degreesCelsius) {
   return (degreesCelsius * (9/5) + 32)
}

function convertFtoC(degreesFahrenheit) {
   return ((degreesFahrenheit-32) * 5/9)
}

function domLoaded() {
   let convertButton = document.getElementById("convertButton")
   let cInput = document.getElementById("cInput")
   let fInput = document.getElementById("fInput")
   let weatherImage = document.getElementById("weatherImage")
   hideImage()
   convertButton.addEventListener("click", convertTemp)
   cInput.addEventListener("input", function(){
      if(fInput.value.length>0){
         fInput.value = ""
      }
   })
   fInput.addEventListener("input", function(){
      if(cInput.value.length>0){
         cInput.value = ""
      }
   })

   function hideImage(){
      weatherImage.style.display = "none"
   }
}

function convertTemp() {
   var cInput = document.getElementById("cInput");
   var fInput = document.getElementById("fInput");
   var weatherImage = document.getElementById("weatherImage");
   var errorMessage = document.getElementById("errorMessage");
   if (cInput.value.length > 0) {// if input not empty
       if (checkErrorInput(cInput.value)) {// runs while input is valid
           fInput.value = convertCToF(parseFloat(cInput.value));
           showImage(parseFloat(fInput.value));// To show respective pngs
       }
   } else if (fInput.value.length > 0) { // if input not empty
       if (checkErrorInput(fInput.value)) { // runs while input is valid
           cInput.value = convertFtoC(parseFloat(fInput.value));
           showImage(parseFloat(fInput.value));// To show respective pngs
       }
   } else {
       errorMessage.innerText = "please enter temperature";
   }

   function checkErrorInput(input) {
       if (isNaN(parseFloat(input))) {
           errorMessage.innerHTML = input + " is not a number";
           return false;  // input is not valid throws error and returns false
       } else {
           errorMessage.innerHTML = "";
           return true;  // valid input
       }
   }

   function showImage(f) {
       if (f < 32) {
           weatherImage.src = "cold.png";// set src attribute to cold gif
           weatherImage.alt = "cold png";
       } else if (f >= 32 && f <= 50) {
           weatherImage.src = "cool.png";//set src attribute to gif
           weatherImage.alt = "cool png";
       } else {
           weatherImage.src = "warm.png"; //set src attribute to gif
           weatherImage.alt = "warm png";
       }
       weatherImage.style.display = "block";

   }
}

window.addEventListener("DOMContentLoaded", domLoaded)