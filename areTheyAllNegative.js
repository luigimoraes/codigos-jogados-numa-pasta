function areTheyAllNegative(numsArray){
    let counter = 0;
    
    for(let number of numsArray){
        if(number < 0){
            counter++;
        }
    }
    
    return (counter==numsArray.length) ? true : false;
}