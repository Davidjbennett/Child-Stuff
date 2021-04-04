window.addEventListener("DOMContentLoaded", function () {
   document.querySelector("#showCircleBtn").addEventListener("click", showCircleClick);
});

function showCircleClick() {
   //! here we use .then to access resolve and print ta da in our div attribute
   //! we sent back. Otherwise we use our .catch method to do our returned reject.
   //! msg in catch can be whatever you choose. What is returned is assigned to msg
   showCircle(160, 180, 120).then((div) => {
      div.innerHTML = 'Ta da!';
      return div;
  }).catch((msg) => {
      alert(msg);
  });
}

// Do not modify the code below

let timerId = null;

function showCircle(cx, cy, radius) {
   
   // Only allow one div to exist at a time
   let div = document.querySelector("div");
   if (div !== null) {
      div.parentNode.removeChild(div);
   }

   // Create new div and add to DOM
   div = document.createElement("div");
   div.style.width = 0;
   div.style.height = 0;
   div.style.left = cx + "px";
   div.style.top = cy + "px";
   div.className = "circle";
   document.body.append(div);

   // Set width and height after showCircle() completes so transition kicks in
   setTimeout(() => {
      div.style.width = radius * 2 + 'px';
      div.style.height = radius * 2 + 'px';		
   }, 10);

   //! promis returns a resolve or reject attribute. We access reslove with
   //! .then and reject with .catch up in our showCircleClick() function
   let promise = new Promise(function(resolve, reject) {
      // Reject if showCircle() is called before timer finishes
      if (timerId !== null) {
         clearTimeout(timerId);
         timerId = null;
         div.parentNode.removeChild(div);
         //! sends phrase back with rejection
         reject("showCircle called too soon");
      }
      else {
         timerId = setTimeout(() => {
            //! send div var which is == to div = document.createElement("div");
            //! back to showCircleClick() function
            resolve(div);
            timerId = null;
         }, 1000);
      }
   });

   return promise;
}