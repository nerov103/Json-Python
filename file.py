import json

'''
JSON string to convert to a Python object
'''
d = '{"name" : "python", "world" : "bangladesh", "year" : "2006"}'

p = json.loads(d)

print(type(p))
print(p)

