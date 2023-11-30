import requests
import yaml


query_params = {"gender": "female", "nat": "de"}
response4 = requests.get("https://randomuser.me/api/", params=query_params).json()
print(type(response4))
print(response4)


'''
r = requests.get("https://api.github.com/users/tater/events")
print(r)
print(r.text)

headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://api.thedogapi.com/v1/breeds", headers=headers)
print(response.headers)
request = response.request
print(request)
print(request.path_url)
print(request.method)
print(request.headers)
print(response.headers.get("Content-Type"))  #узнали, что json
response_json = response.json()
print(len(response_json))
#dict_response = dict(response_json)
b = str(response_json)
#b = b.replace("[", "{").replace("]","}") выдает ошибку
dict_response = yaml.full_load(b) #list
print(type(dict_response))
#b = b[1:-1] #выдает ошибку
#dict_response = {v:k for v,k in enumerate(response_json)}
print(type(dict_response))
print(response_json[0]['weight']) #list
#print(dict_response)
#print(response_json[170])

query_params2 = {"q": "labradoodle"}
endpoint = "https://api.thedogapi.com/v1/breeds/search"
response5 = requests.get(endpoint, params=query_params).json()
print(response5)

'''