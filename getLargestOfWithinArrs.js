function getLargestOfWithinArrs(arr){
    let actualLargest = 0;
    let arrayOfLargest = [];
    
    for(let withinArr of arr){
        actualLargest = withinArr[0];
        for(let number of withinArr){
            if(number > actualLargest){
                actualLargest = number;
            }
        }
        
        arrayOfLargest.push(actualLargest);
    }
    
    return arrayOfLargest;
}