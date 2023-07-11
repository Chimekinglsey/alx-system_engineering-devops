import json

dict_me = {
'person': {"name": 'james', 'age': 20, 'married': True,  '4digitPin': (1, 2, [4, 5, 6])}, 'try': None
}

jdict = json.dumps(dict_me)
jload = json.loads(jdict)
print(dict_me)
print(jdict)
print(jload)
