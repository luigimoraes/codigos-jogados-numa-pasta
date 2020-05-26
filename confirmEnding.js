function confirmEnding(string, match){
    let lastChars = getLastChars(string, match);
    
    return (lastChars == match) ? true : false;
}

function getLastChars(string, target){
    let startPoint = string.length - target.length;
    
    return string.substring(startPoint);
}