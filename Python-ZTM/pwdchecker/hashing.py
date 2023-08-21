#https://docs.python.org/3/library/hashlib.html
import hashlib
# password='123'
# SHA1password = hashlib.sha1(password)
# print(SHA1password)  #--->TypeError: Unicode-objects must be encoded before hashing

password='123'
print(password.encode('utf-8')) #--->b'123'
print(hashlib.sha1(password.encode('utf-8'))) #---><sha1 _hashlib.HASH object @ 0x00000215CE817950>
print(hashlib.sha1(password.encode('utf-8')).hexdigest()) #--->40bd001563085fc35165329ea1ff5c5ecbdbbeef

