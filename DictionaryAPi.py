#This program take a string input and search that word from dictionary API 
# if the word already seached its store that word info in "word-jason" and next time its collect that word  from local folder 
#As a json has a weight of 5-6Kb, 2000 word take only 12Mb, so its easy to keep
# This is done beacuse the api have a maximum call per day, its 1000
# ones that jason data ready this program create there wordlist: synonym, antonym and similar(its also synonym) word.
# If anyone one to increase her vocalbulary its efficent to learn similar word once 
#you can create a list from here  paste the word to vocalbulary.com to practice that 

import requests
import json
import os.path
#from os import path
#import pathlib  

word = input("Write down a single word : ")
#word = 'austere'
word = word.lower()
key = '7444d9af-d1e2-4aab-8e3e-e79c08958d0c' #key got from dictionaryAPi by register. Please try to  get a new key
url = 'https://dictionaryapi.com/api/v3/references/thesaurus/json/' + word+ '?key=' + key
#response = requests.get(url)
#data = response.text

#solve issue 
strpath =  'C:/Users/Anindya/Documents/GitHub/Synonym-/word-json/' + word + '.json'
if os.path.exists(strpath):
    with open(strpath, 'r') as storedfile:
        data = storedfile.read().replace('\n', '')
        storedfile.close()
else:
    response = requests.get(url)
    data = response.text
    storingfile = open(strpath, "x")
    storingfile.write(data)  
    storingfile.close()


parsed = json.loads(data)
#perfectalignment = json.dumps(parsed, indent=4) #create alignment take space but easy to read 
#print(perfectalignment)
strpath =  "C:/Users/Anindya/Documents/GitHub/Synonym-/word-synonym/" + word + ".txt"
file = open(strpath, "w")

synonym = []
count = 0
for synlist in parsed[0]['meta']['syns']:
    for syn in synlist:
        synonym.append(syn)
        file.write(syn + " ")
        if count%10 == 0 :
           file.write("\n")  
print("synonym count: " + str(len(synonym)))
print(synonym)
file.write("\n synonym count: " + str(len(synonym))+ "\n \n")

antonym = []
count = 0
for synlist in parsed[0]['meta']['ants']:
    for syn in synlist:
        antonym.append(syn)
        file.write(syn + " ")
        if count%10 == 0 :
           file.write("\n") 

print("antonym count: " + str(len(antonym)))
print(antonym)
file.write("\n antonym count: " + str(len(antonym))+ "\n \n")

similar = []
similarKey =['rel_list','near_list'] # generally sim_list and syn_list list are already in [meta]syns, so we exclude them
#More similar list
count = 0
sseqList = parsed[0]['def'][0]['sseq']
for sseq in sseqList:
    for key in similarKey:
        if key in sseq[0][1]:
            for synList in sseq[0][1][key]:
                for syn in synList:
                    similar.append(syn['wd'])
similar = list(dict.fromkeys(similar)) #remove duplicate
if len(similar) > 0:
    print("similar word count: " + str(len(similar)))
    print(similar)

count = 0 
for sim in similar:
    file.write(sim + " ")
    if count%10 == 0 :
        file.write("\n")    

file.write("\n similiar count: " + str(len(similar))+ "\n \n")
file.close()
'''
#we dont need this part beacuse its already in meta[ants]; coded for known structure purpose
opposite = []
oppositeKey =['opp_list','ant_list'] # generally exist only one already contains in meta[ants]
#More opposite list
count = 0
sseqList = parsed[0]['def'][0]['sseq']
for sseq in sseqList:
    for key in oppositeKey:
        if key in sseq[0][1]:
            for synList in sseq[0][1][key]:
                for syn in synList:
                    count=count+1
                    oppositeKey.append(syn['wd'])
print("opposite word count: " + str(count))
print(oppositeKey)
'''
#incase we need just synonym and similar word 
''''
Allsynonym = synonym + similar
Allsynonym = list(dict.fromkeys(Allsynonym)) #remove duplicate
print("Total synonym:" + str(len(Allsynonym)))
for syn in Allsynonym:
    print(syn)

'''

