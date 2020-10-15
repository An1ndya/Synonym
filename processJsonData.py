#test purpose ignore it
import json
import os.path
from os import path

word = 'prosaic'
strpath = 'word-json/' + word + '.json'
if path.exists(strpath):
    with open(strpath, 'r') as file:
        data = file.read().replace('\n', '')
else:
    print('false')

parsed = json.loads(data)
#print(parsed)
'''
parsedFormated = (json.dumps(parsed, indent=4))
writeFile = open(word + "-json-formatted.json", "x")
writeFile.write(parsedFormated)
file.close()
writeFile.close()
'''
#print(parsed[0]['meta']['syns'])
#synonym list'

count = 0
for synlist in parsed[0]['meta']['syns']:
    for syn in synlist:
        count=count+1
        print(syn)
print("synonym count: " + str(count))


#More synonym list
count = 0
sseqList = parsed[0]['def'][0]['sseq']
for sseq in sseqList:
    for synList in sseq[0][1]['sim_list']:
        for syn in synList:
            count=count+1
            print(syn['wd'])
print("synonym count: " + str(count))
print(synList)

