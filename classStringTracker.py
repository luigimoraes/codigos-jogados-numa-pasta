#Python 3.7

class StringTracker():
    positionsArray = []
    phrase = ""
    wordToTrack, limiterWord = "", ""
    
    def __init__(self, phrase):
        self.phrase = phrase
        
    def hasWord(self, word):
        start, end = 0, len(word)
    
        while end <= len(self.getPhrase()):
            sli = self.getPhrase()[start:end]
            if sli == word:
                self.positionsArray.append(start)
                self.positionsArray.append(end)
                return True
            else:
                start += 1
                end += 1
                continue
        return False

    def showSlice(self):
        if self.hasWord(self.getLimiterWord()):
            wordToTrackStart, limiterWordEnd = self.getPositionsArray()[0], self.getPositionsArray()[3]
            sli = self.getPhrase()[wordToTrackStart:limiterWordEnd]
            return sli
        else:
            return "Limiter Word not found :/"
    
    def showUntilEnd(self):
        wordTrackStart = self.getPositionsArray()[0]
        phraseTillEnd = self.getPhrase()[wordTrackStart:]
        return phraseTillEnd
    
    def getPositionsArray(self):    return self.positionsArray
    def setPositionsArray(self, positionsArray):    self.positionsArray = positionsArray
    
    def getPhrase(self):    return self.phrase
    def setPhrase(self, phrase):    self.phrase = phrase
    
    def getWordToTrack(self):    return self.wordToTrack
    def setWordToTrack(self, wordToTrack):    self.wordToTrack = wordToTrack
    
    def getLimiterWord(self):    return self.limiterWord
    def setLimiterWord(self, limiterWord):    self.limiterWord = limiterWord
