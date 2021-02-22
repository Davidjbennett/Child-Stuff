function isStrongPassword(passw){
    let hasCap = false
    for(x = 0; x < passw.length; x++){
        // console.log(letter + "\n")
        let letter = passw.charCodeAt(x)
        if(letter >= 65 && letter <= 90){
            hasCap = true
        }    
    }
    if(passw.length >= 8){
        if(passw.indexOf("password") == -1){
            if(hasCap == true){
                return true
            }
        }
    }
    return false
}
