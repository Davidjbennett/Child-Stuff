function check() {
   var fv = true
   var str = ""
   var str1 = ""
   var pat = ""
   var cnfPassword = ""
   var cnfPassword1 = ""
   str = document.getElementById("fullName").value;
   if (str == "") {
       document.getElementById("name_error").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("name_error").style.visibility = "hidden";
       if (fv != false)
           fv = true;
   }
   str = document.getElementById("email").value;
   pat = /^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,4}$/
   if (!pat.test(str)) {
       document.getElementById("email_error").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("email_error").style.visibility = "hidden";
       if (fv == true)
           fv = true;
   }
   str = document.getElementById("password").value;
   str1 = document.getElementById("passwordConfirm").value;
   if (str == "" || str1 == "") {
       document.getElementById("password_empty").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_empty").style.visibility = "hidden";
       if (fv == true)
           fv = true;
   }
   str = document.getElementById("password").value;
   if ((str.length < 10 || str.length > 20) || (str1.length < 10 || str1.length > 20)) {
       document.getElementById("password_len_error").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_len_error").style.visibility = "hidden";
       if (fv == true)
           fv = true
   }

   //uppercase validation
   str = document.getElementById("password").value;
   if (!hasLowerCase(str)) {
       document.getElementById("password_lower").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_lower").style.visibility = "hidden";
       cnfPassword = str
       if (fv == true)
           fv = true
   }

   //lowercase validation
   str = document.getElementById("password").value;
   if (!hasUpperCase(str)) {
       document.getElementById("password_upper").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_upper").style.visibility = "hidden";
       cnfPassword = str
       if (fv == true)
           fv = true
   }

   //uppercase validation
   str = document.getElementById("passwordConfirm").value;
   if (!hasLowerCase(str)) {
       document.getElementById("password_lower").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_lower").style.visibility = "hidden";
       cnfPassword = str
       if (fv == true)
           fv = true
   }

   //lowercase validation
   str = document.getElementById("passwordConfirm").value;
   if (!hasUpperCase(str)) {
       document.getElementById("password_upper").style.visibility = "visible";
       document.getElementById("formErrors").style.display = "block";
       fv = false;
   } else {
       document.getElementById("password_upper").style.visibility = "hidden";
       cnfPassword = str
       if (fv == true)
           fv = true
   }
   return fv;
   function hasLowerCase(str) { //uppercase check
       return (/[a-z]/.test(str));
   }
   function hasUpperCase(str) { //lowercase check
       return (/[A-Z]/.test(str));
   }
}