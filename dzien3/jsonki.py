import json

with open('dane.json') as f:
    person = json.load(f)

print(person['members'][1]["name"])
print(person['members'][1]["powers"][2])



