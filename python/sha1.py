from hashlib import sha1

def make_sha1(s, encoding='utf-8'):
    return sha1(s.encode(encoding)).hexdigest()
    
s = input()
print(make_sha1(s, encoding='utf-8'))