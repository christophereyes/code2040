import requests
import json
import ast

chris_api_token = 'b22eefe6ad7d9acfc8f1bcebf522d11a'
url = 'http://challenge.code2040.org/api/prefix'
payload = {'token': chris_api_token}
r = requests.post(url, json=payload)
dict = ast.literal_eval(r.text)
prefix =  dict.get('prefix')
array = dict.get('array')
print array

def prefix_mod_array(prefix,array):
    strtLen = len(prefix)
    popArray = []
    i = 0
    
    for index in array:
        #print(i,index[0:strtLen])
        if prefix == index[0:strtLen]:
         #   print(prefix,index)
            popArray.append(i)
        i +=1
    popArray.sort(reverse=True)
    print popArray
    arrayL = len(popArray)
    i = 0
    while i < arrayL:
        array.pop(popArray[i])
        i += 1
print(len(array))
prefix_mod_array(prefix,array)
print array
print(len(array))
payload = {'token':chris_api_token,'array':array}
url = 'http://challenge.code2040.org/api/prefix/validate'
requests.post(url, json=payload) 
