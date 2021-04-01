function parseScores(scoresString) {
   return lyst = scoresString.split(" ")
}

function buildDistributionArray(scoresArray) {
   let A = 0
   let B = 0   
   let C = 0   
   let D = 0
   let F = 0
   for(let i of scoresArray){
      if(i >= 90){A++}
      else if(i >= 80 && i < 90){B++}   
      else if(i >= 70  && i < 80){C++}   
      else if(i >= 60 && i < 70){D++}
      else if(i < 60){F++}
   }
   return lyst = [A,B,C,D,F]
}

function setTableContent(userInput) {
   var myTable = document.getElementById("distributionTable")
   if(userInput.length > 0){
      let parsedInfo = parseScores(userInput)
      let buildArr = buildDistributionArray(parsedInfo)
      var row1 = myTable.insertRow(0)
      var row2 = myTable.insertRow(1)
      var row3 = myTable.insertRow(2)
      var cell1 = row2.insertCell(0)
      var cell2 = row2.insertCell(1)
      var cell3 = row2.insertCell(2)
      var cell4 = row2.insertCell(3)
      var cell5 = row2.insertCell(4)
      cell1.innerHTML = "A"
      cell2.innerHTML = "B"
      cell3.innerHTML = "C"
      cell4.innerHTML = "D"   
      cell5.innerHTML = "F"
      var graphArray = []
      var occursArray = []
      for(i = 0; i < 5; i++){
         occursArray[i] = row3.insertCell(i)
         occursArray[i].innerHTML = buildArr[i]
         graphArray[i] = row1.insertCell(i)
         var styleClass = "bar"+i
         var heights = (buildArr[i]*10)+"px"
         graphArray[i].innerHTML = "<div style ='height:" + heights + "' class='" +
                                     styleClass + "'></div>"
         console.log(graphArray[i])
      }
   }else {
      var emptyRow = myTable.insertRow(0).insertCell(0)
      emptyRow.innerHTML = "No graph to display"
   }
}

// The argument can be changed for testing purposes
// setTableContent("45 78 98 83 86 99 90 59");
// setTableContent("")