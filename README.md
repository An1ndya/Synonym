# Synonym
get synonyms of a word by 2 different approach and 3 different source; PyDictionary, WordNet, DictionaryAPI

***DictionaryAPI.py**
#This program take a string input and search that word from dictionary API 
# if the word already seached its store that word info in "word-jason" and next time its collect that word  from local folder 
#As a json has a weight of 5-6Kb, 2000 word take only 12Mb, so its easy to keep
# This is done beacuse the api have a maximum call per day, its 1000
# ones that jason data ready this program create there wordlist: synonym, antonym and similar(its also synonym) word.
# If anyone one to increase her vocalbulary its efficent to learn similar word once 
#you can create a list from here  paste the word to vocalbulary.com to practice that 

***synonym4mPyDictionary.py*****
#This program take a string input and search that word's synonym from pydictionary library
#Its takes another parameter depth 
# the program find all synonyms of given word and the again synonym all of the synonym, so it run like recuresively 
# Just like a graph where head is the word you given
# you gave depth greater than its get too far, maybe we can bind all the word somehow :D
# If anyone one to increase her vocalbulary its efficent to learn similar word once 
#you can create a list from here  paste the word to vocalbulary.com to practice that 

***wordNet.py ***
#have same property , just source is wordnet
