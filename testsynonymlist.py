from PyDictionary import PyDictionary
dictionary=PyDictionary()

word = "hasbbb"

synlist = dictionary.synonym(word)
#print(synlist)

if isinstance(synlist, list): 
    for i in synlist:
       print(i) 





