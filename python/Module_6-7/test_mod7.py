import requests

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
print(response_json) #list
#print(response_json["name"])
