function onPageLoad(){
    //TODO: init controllers
    document.getElementById("rerollBtn").onclick = rerollBtnClicked
    document.getElementById("cancelBtn").onclick = cancelBtnClicked
    document.getElementById("createBtn").onclick = createBtnClicked
    document.getElementById("newCharBtn").onclick = newBtnClicked

    let charList = returnAllCharacters()

    for (let x = 0; x < charList.length; x++){
        addCharListItem(charList[x])
    }

    clearInputForms()
}

function randomRoll(){
    let rando = Math.floor((Math.random() * 6) + 1 +((Math.random() * 6) + 1)+((Math.random() * 6) + 1))
    return rando
}

function rerollBtnClicked(){
    document.getElementById("strength").innerText = randomRoll()   
    document.getElementById("dexterity").innerText = randomRoll()
    document.getElementById("constitution").innerText = randomRoll()
    document.getElementById("intelligence").innerText = randomRoll()
    document.getElementById("wisdom").innerText = randomRoll()
    document.getElementById("charisma").innerText = randomRoll()
}

function newBtnClicked(){
    document.getElementById("characterCreationArea").style.display = "block"
    document.getElementById("characterListArea").style.display = "none"
    document.getElementById("createBtn").style.display = "inline"
    document.getElementById("updateBtn").style.display = "none"

    rerollBtnClicked()
}

function cancelBtnClicked(){
    clearInputForms()
}

function createBtnClicked(){
    if (!validateFields()){
        return
    }

    //TODO: create list of stats
    let statsList = []
    statsList.push(parseInt(document.getElementById("strength").innerText))
    statsList.push(parseInt(document.getElementById("dexterity").innerText))
    statsList.push(parseInt(document.getElementById("constitution").innerText))
    statsList.push(parseInt(document.getElementById("intelligence").innerText))
    statsList.push(parseInt(document.getElementById("wisdom").innerText))
    statsList.push(parseInt(document.getElementById("charisma").innerText))
    

    let form = document.forms["charEditForm"]
    let newChar = createChar(
        form.charName.value,
        form.raceSelection.value,
        form.classSelection.value,
        form.gender[0].checked,
        form.rightHanded.checked,
        statsList
    )

    addCharListItem(newChar)

    clearInputForms()
}

function onEditBtnClick(id){
    let playerChar = findCharacter(id)
    if(!playerChar){
        alert("Unable to find character.")
    }

    document.getElementById("formTitle").innerText = "Edit Character"
    
    let form = document.forms["charEditForm"]

    form.charName.value = playerChar.name
    
    document.getElementById("strength").innerText = playerChar.stats[0]    
    document.getElementById("dexterity").innerText = playerChar.stats[1]  
    document.getElementById("constitution").innerText = playerChar.stats[2]  
    document.getElementById("intelligence").innerText = playerChar.stats[3]  
    document.getElementById("wisdom").innerText = playerChar.stats[4]  
    document.getElementById("charisma").innerText = playerChar.stats[5]  
    
    for (let race in form.raceSelection.options){
        let option = form.raceSelection.options[race]
        if(option.value === playerChar.race){
            option.selected = true
        }
    }
    for (let clss in form.classSelection.options){
        let option = form.classSelection.options[clss]
        if(option.value === playerChar.clss){
            option.selected = true
        }
    }

    if (playerChar.male){
        form.gender[0].checked = true
    }else {
        form.gender[1].checked = true
    }
    form.rightHanded.checked = playerChar.righthanded

    document.getElementById("characterCreationArea").style.display = "block"
    document.getElementById("characterListArea").style.display = "none"
    document.getElementById("createBtn").style.display = "none"

    let updateBtn = document.getElementById("updateBtn")
    updateBtn.style.display = "inline"
    updateBtn.onclick = function() {
        onUpdateBtnClick(playerChar.id)
    }
}

function onUpdateBtnClick(id){
    if (!validateFields()){
        return
    }

    //TODO: create list of stats
    let statsList = []
    statsList.push(parseInt(document.getElementById("strength").innerText))
    statsList.push(parseInt(document.getElementById("dexterity").innerText))
    statsList.push(parseInt(document.getElementById("constitution").innerText))
    statsList.push(parseInt(document.getElementById("intelligence").innerText))
    statsList.push(parseInt(document.getElementById("wisdom").innerText))
    statsList.push(parseInt(document.getElementById("charisma").innerText))
    

    let form = document.forms["charEditForm"]
    let newChar = updatePlayerChar(
        id,
        form.charName.value,
        form.raceSelection.value,
        form.classSelection.value,
        form.gender[0].checked,
        form.rightHanded.checked,
        statsList
    )
    
    if(!newChar){
        alert("Unable to update character")
    }

    let tr = document.getElementById("row"+newChar.id)
    tr.childNodes[0].innerText = newChar.name
    tr.childNodes[1].innerText = newChar.race
    tr.childNodes[2].innerText = newChar.clss
    tr.childNodes[3].innerText = newChar.male? "Male":"Female"

    clearInputForms() 
}

function onDeleteBtnClick(id){
    let playerChar = findCharacter(id)
    if(!playerChar){
        alert("Unable to find character")
        return
    }

    if(!confirm("Are you sure you want to delete " + playerChar.name + "?")){
        return
    }

    deletePlayerChar(id)

    let tr = document.getElementById("row"+id)
    tr.remove()
}

function validateFields(){
    let form = document.forms["charEditForm"]
    let isValid = true

    //Name Validation
    if(form.charName.value === ""){
        document.getElementById("charNameError").innerText = "*Enter a name"
        document.getElementById("charNameError").style.color = "red"
        isValid = false
    } else{
        document.getElementById("charNameError").innerText = ""
        document.getElementById("charNameError").style.color = "black"
    }

    //Race Validation
    if( form.raceSelection.selectedIndex === -1){
        document.getElementById("playerRaceError").innerText = "*Select Race"
        document.getElementById("playerRaceError").style.color = "red"
        isValid = false
    }else{
        document.getElementById("playerRaceError").innerText = ""
        document.getElementById("playerRaceError").style.color = "black"
    }

    //Class Validation
    if( form.classSelection.selectedIndex === -1){
        document.getElementById("playerClassError").innerText = "*Select Class"
        document.getElementById("playerClassError").style.color = "red"
        isValid = false
    }else{
        document.getElementById("playerClassError").innerText = ""
        document.getElementById("playerClassError").style.color = "black"
    }

    //Gender Validation
    if(!form.gender[0].checked && !form.gender[1].checked){
        document.getElementById("genderError").innerText = "*Select a gender"
        document.getElementById("genderError").style.color = "red"
        isValid = false
    }else{
        document.getElementById("genderError").innerText = ""
        document.getElementById("genderError").style.color = "black"
    }

    return isValid
}

function addCharListItem(playerChar){
    let table = document.getElementById("charTable")

    let row = table.insertRow(table.rows.length)
    row.id = "row" + playerChar.id

    let cell0 = row.insertCell(0)
    cell0.innerText = playerChar.name

    let cell1 = row.insertCell(1)
    cell1.innerText = playerChar.race

    let cell2 = row.insertCell(2)
    cell2.innerText = playerChar.clss

    let cell3 = row.insertCell(3)
    cell3.innerText = playerChar.male ? "Male" : "Female"

    let editBtn = document.createElement("button")
    editBtn.type = "button"
    editBtn.className = "editBtn"
    editBtn.innerText = "Edit"
    editBtn.onclick = function() {
        onEditBtnClick(playerChar.id)
    }
    cell4 = row.insertCell(4)
    cell4.appendChild(editBtn)
    

    let deleteBtn = document.createElement("button")
    editBtn.type = "button"
    deleteBtn.innerText = "Delete"
    deleteBtn.className = "deleteBtn"
    deleteBtn.onclick = function() {
        onDeleteBtnClick(playerChar.id)
    }
    cell5 = row.insertCell(5)
    cell5.appendChild(deleteBtn)
}

function clearInputForms(){
    document.getElementById("characterCreationArea").style.display = "none"
    document.getElementById("characterListArea").style.display = "block"

    let form = document.forms["charEditForm"]

    form.charName.value = ""
    document.getElementById("charNameError").innerText = ""

    document.getElementById("strength").innerText = " "
    document.getElementById("dexterity").innerText = " "
    document.getElementById("constitution").innerText = " "
    document.getElementById("intelligence").innerText = " "
    document.getElementById("wisdom").innerText = " "
    document.getElementById("charisma").innerText = " "
    
    form.raceSelection.selectedIndex = -1
    document.getElementById("playerRaceError").innerText = ""
    
    form.classSelection.selectedIndex = -1
    document.getElementById("playerClassError").innerText = ""

    form.gender[0].checked = false
    form.gender[1].checked = false
    document.getElementById("genderError").innerText = ""

    form.rightHanded.checked = false
    
}