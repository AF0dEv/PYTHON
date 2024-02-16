import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    # print(d1_json)
    d1_json = json.loads(d1_json) # Tem que ter nome Igual
    # print(d1_json)

for k, v in d1_json.items():
    print(k, v) # k = key / v = value
    for k1, v1 in v.items():
        print(k1, v1)