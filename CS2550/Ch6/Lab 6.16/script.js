function drawTriangle(n) {
   var result = "";
   for (var i = 0; i < n; i++) {
       for (var j = 0; j <= i; j++) {
           result += "*";
       }
       if (i !== n - 1)
           result += "\n";
   }
   console.log(result);
}
