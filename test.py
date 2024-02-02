
import json


json_deta = 'Hello Wow Are You?'
#convet to json
make_json = json.dumps(json_deta)
# print(type(make_json))

make_pyobj = json.loads(make_json)

# ex = json.loads(json_deta)
print(type(make_pyobj))





