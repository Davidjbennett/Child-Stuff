let charList = []
let nextId = 1

function playerCharacter(name, race, clss, male, righthanded, stats){
    this.id = nextId++
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

function updatePlayerChar(id, name, race, clss, male, righthanded, stats){
    let playerChar =  findCharacter(id)
    if (!playerChar){
        return undefined
    }

    playerChar.name = name
    playerChar.race = race
    playerChar.clss = clss
    playerChar.male = male
    playerChar.righthanded = righthanded
    playerChar.stats = stats

    return playerChar
}

function deletePlayerChar(id){
    for (let x in charList){
        if(charList[x].id === id){
            charList.splice(x,1)
            break;
        }
    }
}

function findCharacter(id){
    for (let x in charList){
        if(charList[x].id === id){
            return charList[x]
        }
    }
    return undefined
}