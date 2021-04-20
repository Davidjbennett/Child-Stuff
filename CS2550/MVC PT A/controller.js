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
        form.genderMale.checked,
        form.rightHanded.checked,
        statsList
    )

    addCharListItem(newChar)

    clearInputForms()
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
    if(!form.genderMale.checked && !form.genderFemale.checked){
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

    let cell0 = row.insertCell(0)
    cell0.innerText = playerChar.name

    let cell1 = row.insertCell(1)
    cell1.innerText = playerChar.race

    let cell2 = row.insertCell(2)
    cell2.innerText = playerChar.clss

    let cell3 = row.insertCell(3)
    cell3.innerText = playerChar.male ? "Male" : "Female"
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

    form.genderMale.checked = false
    form.genderFemale.checked = false
    document.getElementById("genderError").innerText = ""

    form.rightHanded.checked = false
    
}