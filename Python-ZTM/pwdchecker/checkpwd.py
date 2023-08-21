#https://docs.python.org/3/library/hashlib.html
import requests
import hashlib
# url='https://api.pwnedpasswords.com/range/' + 'E38AD'
# res=requests.get(url)
# print(res)
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the API and try again')
    return res # <Response [200]>
"""
response=request_api_data(first5_char)
# we get all the hashes that match the begining of our hashed password
So, here in the response, we get just the tails of the hashes which 1st 5 chars match with our first5_char of hashed password.
for example:
password='123'
its hash is 40bd001563085fc35165329ea1ff5c5ecbdbbeef
now we send request_api_data('40bd0') and we get in response 01563085FC35165329EA1FF5C5ECBDBBEEF (one of the responses)
"""
def read_res(response):
    print(response.text)# as it is API response, we should use .text to read it
    '''by using response.txt, we get all the hashes that match the begining of our haashed password'''

def pwned_api_check(password):
    #check if the password exists in the API response
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #In order to agree with the API, we need to convert all of the hash to uppercase.
    print(sha1password) #passsword:'123' - Hash:40BD001563085FC35165329EA1FF5C5ECBDBBEEF
    first5_char, tail_char = sha1password[:5], sha1password[5:]
    print(first5_char, tail_char)
    response=request_api_data(first5_char)
    print(response) # <Response [200]>
    # print(response.txt)
    return read_res(response)

pwned_api_check("123")

"""
01563085FC35165329EA1FF5C5ECBDBBEEF:1078184 ---it means the password having this hash had been hacked 1078184 times
"""