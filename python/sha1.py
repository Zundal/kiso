import hashlib
h = hashlib.new('sha1')
h.update(b"Baekjoon")

print(h.hexdigest())