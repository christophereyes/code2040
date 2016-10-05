import requests
import json

chris_api_token = 'b22eefe6ad7d9acfc8f1bcebf522d11a'
#github_address = 'https://github.com/christophereyes/code2040.git'
payload = {'token':chris_api_token}
url = 'http://challenge.code2040.org/api/reverse'


#print(chris_api_token, github_address)

r = requests.post(url, json=payload)
print(r.text)
print(r)
#jsn = r.json()
#token = r.json()
#payload = {"token" : token["result"], "string" :jsn["result"][::-1]}
string = r.text
print(string)
print(string[::-1])
payload = {'token':chris_api_token, 'string': string[::-1]}
r = requests.post("http://challenge.code2040.org/api/reverse/validate", json = payload)

