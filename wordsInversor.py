#Python 3.6
#Inverts words in phrase without inverts
#the order of words in phrase

phrase = input("= ")
init, end = 0, 0
last, newPhrase = phrase[len(phrase)-1:len(phrase)], ""

for char in phrase:
    sli = phrase[init:end]
    if char.isspace() == True:
        newPhrase += sli[::-1]+" "
        init = end + 1
    elif char is last and end == len(phrase)-1:
        newPhrase += last+sli[::-1]
    end += 1

print(newPhrase)