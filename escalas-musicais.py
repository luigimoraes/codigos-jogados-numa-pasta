# Python 3.8
# Criar escalas musicais com base em uma so nota

sustenidos = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
bemois = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
majorScale, minorScale = [], []

def orderScale(tone, chromaticScale):
	note = chromaticScale.index(tone)
	scaleFirstSlice = chromaticScale[note:]
	scaleLastSlice = chromaticScale[:note]
	
	orderedScale = scaleFirstSlice + scaleLastSlice
	return orderedScale

def createMajorScale(chromaticScale):
	noteIndex = 0
	while(noteIndex <= 11):
		majorScale.append(chromaticScale[noteIndex])
		if(noteIndex==4):	noteIndex+=1
		else:	noteIndex+=2
	return majorScale

def createMinorScale(chromaticScale):
	noteIndex = 0
	while(noteIndex <= 11):
		minorScale.append(chromaticScale[noteIndex])
		if(noteIndex==2 or noteIndex==7):	noteIndex+=1
		else:	noteIndex+=2
	return minorScale

tom=input("Digite o tom da escala: ")
orderedScale = orderScale(tom, sustenidos)

scale = createMajorScale(orderedScale)

print("Escala de "+tom+" Maior: ", scale)