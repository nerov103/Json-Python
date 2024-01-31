import json

'''
What are JSON loads () in Python?
The json.loads() method can be used to parse a valid JSON string 
and convert it into a Python Dictionary. 
It is mainly used for deserializing native string, byte,
or byte array which consists of JSON data into Python Dictionary.

Syntax : json.loads(s)

Argument: It takes a string, bytes,
or byte array instance which contains the JSON document as a parameter (s).
'''

son_string = '{"name": "Alice", "age": 30, "city": "New York"}'

print(type(son_string))


x = json.loads(son_string)

print(type(x))



