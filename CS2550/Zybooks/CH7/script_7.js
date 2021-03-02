//!Challenges
/*Register the textChanged event handler to handle blur
changes for the input tag. Note: The function counts the
number of characters in the input.

HTML
<label for="userName">User name:</label>
<input id="userName" type="text"><br>
<p id="stringLength">0</p>

JS
let inputElement = document.getElementById("userName");

function textChanged(event) {
   document.getElementById("stringLength").innerHTML = event.target.value.length;
}

inputElement.addEventListener("blur", textChanged)




Write and register an event handler that displays "Event fired"
on the console log when the p receives a mousemove event.

HTML: 
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
<p>Paragraph</p>
<a href="https://www.example.com">Example.com</a>

JS
let pElement = document.getElementsByTagName("p")[0];

function eventFired(event){
   console.log("Event fired")
   }
   
pElement.addEventListener("mousemove", eventFired)



Write and register an event handler that changes
the color of the h1 tag to gold on mousemove.

same html as 2nd

JS
let h1Element = document.getElementsByTagName("h1")[0];
  
h1Element.addEventListener("mousemove", function(){h1Element.style.color = 'gold'})


Write a setTimeout() function that reveals the answer after 3 seconds.
JS
function revealAnswer() {
  let answerElement = document.getElementsByClassName("answer")[0];

   answerElement.style.display = "block";
}

setTimeout(revealAnswer,3000);



Write a setInterval() function that updates the progress bar every 
400 milliseconds.

JS
const  progressIndicator = document.getElementById("progress");
let progress;
let timerId;

let startButton = document.getElementById("startBtn");
startButton.addEventListener("click", startDownload);

function addProgress() {
   progress += 20;
   progressIndicator.style.width = progress + "px";
        
   if (progress >= 100) {
      clearInterval(timerId);
   }
}

function startDownload() {
   progress = 0;
   progressIndicator.style.width = progress;
   timerId = setInterval(addProgress, 400);
}



Write a setInterval() function that increases the count by 1
and displays the new count in counterElement every 300 milliseconds.
Call clearInterval() to cancel the interval when the count displays 5.

JS
let count = 0;
let counterElement = document.getElementById("counter");
counterElement.innerHTML = count;

let interval = setInterval(function(){
   count++
   counterElement.innerHTML = count
   if(count==5){
      clearTimeout(interval)
      }
   },300)



*/

//! Scattered Code on Zyb
/*
Text:
The web page below displays a menu of food items with 3 buttons underneath:

Insert Rule button - Calls insertRule() to add a new paragraph rule that 
turns the menu items' font color blue.
Change Rule button - Calls changeRule() to change the paragraph rule's color
to red.
Delete Rule button - Calls deleteRule() to delete the paragraph rule, which
turns the font color back to green.
Click the three buttons in order to watch the font color change from green 
to blue, blue to red, and finally back to green.

Make the following modifications:

Add code to insertRule() that inserts the rule .price { font-weight: bold; } 
so the prices appear bold.
Add code to changeRule() that changes the .price rule to include the property 
font-style set to italic so the prices appear bold and italic.
Add code to deleteRule() that deletes the .price rule so the font weight and 
style returns to normal.
After making the modifications, click the 3 buttons in order to verify the 
price font changes as expected.

HTML:
<body>
   <div id="menu">
      <h1>Menu</h1>
      <p>
         Ham sandwich - <span class="price">$5</span>
      </p>
      <p>
         Spinach salad - <span class="price">$4.50</span>
      </p>
      <p>
         Hamburger - <span class="price">$5.50</span>
      </p>
   </div>
   
   <p>
      <button id="insertRuleBtn">Insert Rule</button>
      <button id="changeRuleBtn">Change Rule</button>
      <button id="deleteRuleBtn">Delete Rule</button>      
   </p>
</body>


CSS:
body  {
   color: darkgreen;
   font-family: Arial, Helvetica, sans-serif;
}

#menu {
   background-color: moccasin;
   width: 200px;        
   text-align: center;
   padding: 10px;
   border-radius: 20px;
}


JS:
document.querySelector("#insertRuleBtn").addEventListener("click", insertRule);
document.querySelector("#changeRuleBtn").addEventListener("click", changeRule);
document.querySelector("#deleteRuleBtn").addEventListener("click", deleteRule);
   
function insertRule() {    
   // Insert paragraph rule
   let stylesheet = document.styleSheets[0];
   stylesheet.insertRule("p { color: blue; }");
   
   // Insert .price rule
   
}

function changeRule() { 
   // Change paragraph rule
   let stylesheet = document.styleSheets[0];
   for (let i = 0; i < stylesheet.cssRules.length; i++) {                
      if (stylesheet.cssRules[i].selectorText === "p") {
         let style = stylesheet.cssRules[i].style;        
         style.setProperty("color", "red");
      }
   }
   
   // Change .price rule
}

function deleteRule() {    
   // Delete the paragraph rule
   let stylesheet = document.styleSheets[0];
   for (let i = 0; i < stylesheet.cssRules.length; i++) {                
      if (stylesheet.cssRules[i].selectorText === "p") {
         stylesheet.deleteRule(i);
      }
   }
   
   // Delete .price rule
   
}




Text:
The web page below asks the user to enter a strong password that meets 
3 criteria. When the user clicks the Submit button, the isStrongPassword()
 is called with the password entered.

If the password does not meet all 3 criteria, isStrongPassword() returns 
false and an error message is displayed by removing the hidden class from 
the error message.
If the password meets all 3 criteria, isStrongPassword() returns true and 
the hidden class is added to the error message to hide the error message.
Enter some passwords that cause the error message to be visible and then
 hidden. Ex: Enter "abc" and press Submit to see the error message, then 
 "abcdef1" to hide the error message.

Modify the submitBtnClick() function to do the following:

If isStrongPassword() returns true, then remove the error-textbox class from
 the password text box.
If isStrongPassword() returns false, then add the error-textbox class to the 
password text box.
After making the modifications, verify the password text box is highlighted 
in red only when entering an invalid password.

For an extra challenge, add the error class to the criteria that is violated 
when an invalid password is entered. Ex: If the password is not long enough,
 add the error class to the first <li> so the item becomes red.

 HTML:
<body>
   <p>Choose a strong password that meets the following criteria:
   </p>
   <ol>
      <li>At least 6 characters long.</li>
      <li>Contains at least 1 digit.</li>
      <li>Is not "password1".</li>
   </ol>
   <form>
      <label for="password">Password:</label>
      <input type="text" id="password">
      <span class="error hidden" id="errorMsg">Invalid password</span>
      <div>
         <input type="button" id="submitBtn" value="Submit">
      </div>
   </form>
</body>

CSS:
.hidden {
   display: none;
}

.error {
   color: red;
}

.error-textbox {
   border: 2px solid red;
   border-radius: 4px;
}

JS:
document.querySelector("#submitBtn").addEventListener("click", submitBtnClick);

function isStrongPassword(password) {
   return password.length >= 6 && /\d/.test(password) && password !== "password1";
}

function submitBtnClick() {
   let password = document.querySelector("#password").value;
   if (isStrongPassword(password)) {
      document.querySelector("#errorMsg").classList.add("hidden");
      
      // Remove error-textbox class

   } else {
      document.querySelector("#errorMsg").classList.remove("hidden");

      // Add error-textbox class

   }
}


*/
