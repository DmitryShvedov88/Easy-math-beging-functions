import requests
r=requests.get("http://example.com") #get request
print(r.text)

url="http://example.com"
par={"key1": "value1", "key2": "value2"}
r=requests.get(url, params=par) #passing parameters to the request
print(r.url)#generated url request

