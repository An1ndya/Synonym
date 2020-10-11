from nltk.corpus import wordnet   #Import wordnet from the NLTK

'''Collected from wornet blog
synset = wordnet.synsets("austere")
for syn in wordnet.synsets("austere"):
    for l in syn.lemmas():
        synonyms.append(l.name())

print(set(synonyms))
'''
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
        if not len(word.split()) > 1:
            synlist = wordnet.synsets(word)
            if isinstance(synlist, list):             
                for synword in synlist:
                    for l in synword.lemmas():
                        if not len(l.name().split()) > 1:
                            Synonym(l.name(),loopcount+1,maxloopcount) 
                return 
            return
        return
    return
    

Synonym(word,0,depth)
#print(dictionary.synonym(word))
print("Total words: " + str(len(wordlist)))
for i in wordlist:
    print(i)


