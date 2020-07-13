def PigLatinator(sentence): 
    vowels = ["a", "e", "i", "o", "u", "y"]
    backlist = []
    finalsentence = ""
    for word in sentence:
        if word[0] in vowels:
            backlist.append(word+"way")              
        else:
            x= 0
            for i in word:
                if i not in vowels:
                    x+= 1
                if i in vowels:
                    prefix =(word[x:])
                    backlist.append(prefix+word[0:x]+"ay")
                    break
    for s in backlist:
        finalsentence+= (s+" ")
    print(finalsentence)

SentenceInput = input(">> ").split(" ")

PigLatinator(SentenceInput)

