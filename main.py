import json

with open('new_file.json', 'r') as json_f:
    a = json.load(json_f)


print(a)
