#https://haveibeenpwned.com/
#https://passwordsgenerator.net/sha1-hash-generator/

'''
In general we never give the exact password to check in the APIS, we give the Hash of our password,
so the even when the password leakage happens they can't get the password as it will be in the form of Hash. But, if we give the Hash of our entire password by some trial and error
they can find out our original password if they get the hash. In order to avoid this, we use K-anonymity.
K-anonymity is a key concept that was introduced to address the risk of re-identification of anonymised data through
linkage to other datasets. So, we only give 1st 5 characters of our Hash to the APIs.
'''
'''
We only give the 1st 5 characters of our hash password,now what this API (pwned API) is going to do is it has a list of all the passwords that have been leaked.
However, all those passwords are hashed with the SHA1 algorithm.
So it's going to look in its database of all these passwords and pick all the hashed passwords that have the first five characters that match our 1st 5 chars.
So this way, with the response, we're going to get all the passwords that are hashed that have our 1st 5 chars.
so that on our end, when we receive that response, we can check the rest of the hash function. This way API is never going to know our full hash and therefore never, ever be able to guess our password.

'''
import requests
url='https://api.pwnedpasswords.com/range/' + 'password123' #only hash should be given as input to the API, here we had given some string hence it will give 400 code
res=requests.get(url)
print(res)
import requests
url='https://api.pwnedpasswords.com/range/' + 'E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D' #only 5 hash characters should be given as input to the API, hence it will give 400 code
res=requests.get(url)
print(res)
import requests
url='https://api.pwnedpasswords.com/range/' + 'E38AD'
res=requests.get(url)
print(res) #<Response [200]> --- Perfect!!!
#'E38AD214943DAAD1D64C102FAEC29DE4AFE9DA3D' is the SHA1 Hash of 'password1'
'''range is just part of the URL. In this case, it's how this particular part of the API is accessed. In API terms it's called an endpoint. 
When you access range/E38AD the server interprets that request, executes a query, and returns results.'''

