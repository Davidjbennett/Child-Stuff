
function divideArray(numbers){
    let evenNums = []
    let oddNums = []

    for(i = 0; i < numbers.length; i++){
        if(numbers[i]%2 == 0){
            evenNums.push(numbers[i])
        } 
        else if(numbers[i]%2 == 1){
            oddNums.push(numbers[i])
        }
    }
    // Sort Even and Odd Array
    evenNums.sort(function(a,b){return a-b;})
    oddNums.sort(function(a,b){return a-b;})

    //Output Even and Odd array
    console.log("Even numbers:")
    if(evenNums.length == 0){
        console.log("None")
    }
    else{
        for(i = 0; i < evenNums.length; i++){
            console.log(evenNums[i])
        }
    }

    console.log("Odd numbers:")
    if(oddNums.length == 0){
        console.log("None")
    }
    else{
        for(i = 0; i < oddNums.length; i++){
            console.log(oddNums[i])
        }
    }
    
}

let nums = [4, 2, 9, 1, 8];
divideArray(nums);
