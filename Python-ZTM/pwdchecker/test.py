import requests
import hashlib
import sys

query_char='40bd0'
url = 'https://api.pwnedpasswords.com/range/' + query_char
res = requests.get(url)
if res.status_code != 200:
    raise RuntimeError(f'Error fetching:{res.status_code}, check the API and try again')
print(res) #---><Response [200]>


password = '123'
sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
print(sha1password)  # passsword:'123' - Hash:40BD001563085FC35165329EA1FF5C5ECBDBBEEF
first5_char, tail_char = sha1password[:5], sha1password[5:]
print(first5_char, tail_char)
url = 'https://api.pwnedpasswords.com/range/' + first5_char
res = requests.get(url)
if res.status_code != 200:
    raise RuntimeError(f'Error fetching:{res.status_code}, check the API and try again')
print(res.text)
print(res.text.splitlines())
lst=[]
for i in res.text.splitlines():
    lst.append(i.split(':'))
print(lst)