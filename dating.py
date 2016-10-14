import requests
import json
import ast
from datetime import datetime, timedelta

chris_api_token = 'b22eefe6ad7d9acfc8f1bcebf522d11a'
url = 'http://challenge.code2040.org/api/dating'
payload = {'token': chris_api_token}
r = requests.post(url, json=payload)
dict = ast.literal_eval(r.text)
datestamp = dict.get('datestamp')
interval = dict.get('interval')#value returned is that of the seconds needed to convert and add to datestamp
m, s = divmod(interval, 60)#converst seconds to minutes and leaves remaining seconds to var s
h, m = divmod(m , 60)#same as previous line but for hours and minutes
days, h = divmod(h, 24)#once again same but for days and hours...hey seems like recursion could be at play

def vars_to_var(days,hours,mins,secs):#function attempting to create a new datetime value to add to previous datetime value in datetime types
    d = str(days)
    h = str(hours)
    m = str(mins)
    s = str(secs)
    var_time = d +'T'+h+':'+m+':'+s+'Z'
    print(var_time)
    var_time = datetime.strptime(var_time, "%dT%H:%M:%SZ")
    return var_time#ultimately this funtion does not get used

def add_vars(org_date,dys,hrs,mins,secs):#goes through the four values of days,hours,minutes and seconds and uses the timedelta method to add to datestamp parameter
    print(org_date)
    org_date += timedelta(seconds=secs)
    print(org_date)
    org_date += timedelta(minutes = mins)
    print(org_date)
    org_date += timedelta(hours = hrs)
    print(org_date)
    org_date += timedelta(days = dys)
    print(org_date)
    return org_date#return of new datestamp value after all time variables are added

datestamp = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")#var datestamp is converted to a datestamp value



datestamp = add_vars(datestamp, days, h, m, s)
datestamp = datestamp.strftime("%Y-%m-%dT%H:%M:%SZ")#method strftime converting datestamp from datetime type back to string in proper notation
url = 'http://challenge.code2040.org/api/dating/validate'

payload = {'token':chris_api_token, 'datestamp': datestamp}
r = requests.post(url, json=payload)
print(r.text)
