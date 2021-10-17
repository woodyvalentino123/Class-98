def wordsFromFile():
    fileName=input("Enter The Name Of The File: ")
    file=open(fileName,'r')
    numberOfWords=0
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords + len(words)

    print("Number of words: ")
    print(numberOfWords)

wordsFromFile()