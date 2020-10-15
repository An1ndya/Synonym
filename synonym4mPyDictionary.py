#This program take a string input and search that word's synonym from pydictionary library
#Its takes another parameter depth 
# the program find all synonyms of given word and the again synonym all of the synonym, so it run like recuresively 
# Just like a graph where head is the word you given
# you gave depth greater than its get too far, maybe we can bind all the word somehow :D
# If anyone one to increase her vocalbulary its efficent to learn similar word once 
#you can create a list from here  paste the word to vocalbulary.com to practice that 

from PyDictionary import PyDictionary
dictionary=PyDictionary()


word = input("Write down a single word: ")
depth = input("Number of depth you want to traverse by synonym(try less than 5): ")
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
