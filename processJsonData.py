import json



with open('word-json/austere-json.txt', 'r') as file:
    data = file.read().replace('\n', '')
parsed = json.loads(data)
#print(parsed)
parsedFormated = (json.dumps(parsed, indent=4))
writeFile = open("austere-json-formatted.txt", "x")
writeFile.write(parsedFormated)
file.close()
writeFile.close()
