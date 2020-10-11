import json



with open('austere-json.txt', 'r') as file:
    data = file.read().replace('\n', '')
parsed = json.loads(data)
print(parsed)
#print(json.dumps(parsed, indent=4))
