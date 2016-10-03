import requests
import json

chris_api_token = 'b22eefe6ad7d9acfc8f1bcebf522d11a'
github_address = 'https://github.com/christophereyes/code2040.git'
payload = {'token':chris_api_token, 'github': github_address}
url = 'http://challenge.code2040.org/api/register'

print(payload)

print(chris_api_token, github_address)

r = requests.post(url, json=payload)

print(r)
print(r.text)
r.json()

