let charList = []

function playerCharacter(name, race, clss, male, righthanded, stats){
    this.name = name
    this.race = race
    this.clss = clss
    this.male = male
    this.righthanded = righthanded
    this.stats = stats
}

function createChar(name, race, clss, male, righthanded, stats){
    let newChar = new playerCharacter(name, race, clss, male, righthanded, stats)
    charList.push(newChar)
    //return new char so createBTN can take char obj and call addCharListItem(playerChar)
    return newChar
}

function returnAllCharacters(){
    return charList
}

// function findCharacter(){}