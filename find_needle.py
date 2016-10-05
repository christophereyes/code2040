import requests
import ast
import json

chris_api_token = 'b22eefe6ad7d9acfc8f1bcebf522d11a'
url = 'http://challenge.code2040.org/api/haystack'

payload = {'token':chris_api_token}

r = requests.post(url, json=payload)

dict = ast.literal_eval(r.text)
needle = dict.get('needle')
haystack = dict.get('haystack')
print(needle)
#print(haystack)
index = 0

#for index in haystack:
 #   if needle == index:
  #      print(index)


def where_stack(haystack, needle):
    i = 0
    for index in haystack:
        if needle == index:
            print(index, i)
            return i
        i += 1

index = where_stack(haystack, needle)
#print "This is returned value %d" % index

url = 'http://challenge.code2040.org/api/haystack/validate'
payload = {'token':chris_api_token, 'needle':index}
requests.post(url, data=payload)
