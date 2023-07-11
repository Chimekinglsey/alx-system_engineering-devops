import json

dict2 = {'name' : {'surname': "Ibe", 'Middle_name' : "Chiduben"}, 'age' : 25, 'married' : True, 'kids': None}

def to_json():
	json_string = json.dumps(dict2)
	return json_string


def from_json():
	json_string2 = json.loads(json_string)
	return json_string2

to_json()
from_json()
