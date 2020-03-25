#Python 3.6

oldFile = open("path/to/old/file").readlines()
newFile = open("path/of/new/file", "w")

for line in oldFile:
    for char in line:
        if char=='>' or char==';':
            newFile.write(char+"\n\t")
        elif char=='}':
            newFile.write("\n"+char+"\n")
        else:
            newFile.write(char)

newFile.close()