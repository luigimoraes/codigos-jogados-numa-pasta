function repeatNumTimes(str, num){
    let auxString = str;
    const LIMIT = num-1;
    
    for(let counter=1; counter <= LIMIT; counter++){
        str += auxString;
    }
    
    return str;
}