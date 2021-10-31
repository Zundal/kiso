import base64
sitename = input()
sitename_bytes = sitename.encode('ascii')
sitename_base64 = base64.b64encode(sitename_bytes)
sitename_base64_str = sitename_base64.decode('ascii')
print(str(sitename_base64_str))