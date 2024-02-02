import json

'''
Python object to convert to JSON.
'''
web = {"url" : "www.google.com","name" : "google",
       "desh": "bangladesh",
       "year": 2006
       }

f = json.dumps(web)

print(type(f))

print(f)


