function findLongestWordLength(phrase){
		let wordsArray = phrase.split(" ");
		let actualBiggerLength = 0;

		for(let word of wordsArray){
				if(word.length>actualBiggerLength){
						actualBiggerLength = word.length;
				}
		}

		return actualBiggerLength;
}

write(findLongestWordLength("um dois três quatro"));