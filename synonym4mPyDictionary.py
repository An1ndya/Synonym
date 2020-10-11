from PyDictionary import PyDictionary
dictionary=PyDictionary()


word = input("Write down a single word: ")
depth = input("Number of depth you want to traverse by synonym: ")
#word = "austere"
#depth = 3
wordlist =list()
def Synonym(word, loopcount, maxloopcount):
    
    if loopcount == maxloopcount:
        if not  word in wordlist:
            wordlist.append(word) 
        return
    if not  word in wordlist:
        wordlist.append(word) 
        #print(word)
        if not len(word.split()) > 1:
            synlist = dictionary.synonym(word)
            if isinstance(synlist, list):             
                for synword in synlist:
                    if not len(word.split()) > 1:
                        Synonym(synword,loopcount+1,maxloopcount)  
                return 
            return
        return
    return
    

Synonym(word,0,depth)
#print(dictionary.synonym(word))
print("Total words: " + str(len(wordlist)))
for i in wordlist:
    print(i)
