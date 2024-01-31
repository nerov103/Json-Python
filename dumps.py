import json


'''
Converts a Python object (dictionary, list, string, etc.)
into a JSON string
'''
import json

data = {"name": "Bob", "age": 25, "hobbies": ["music", "reading", "sports"]}

convert_json = json.dumps(data)
print(type(convert_json))  # Output: '{"name": "Bob", "age": 25, "hobbies": ["music", "reading", "sports"]}'
print(convert_json)


