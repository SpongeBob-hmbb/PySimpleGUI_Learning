import base64
f = open(r"\.png","rb") # 路径
res = f.read()
s = base64.b64encode(res)
print(s)
f.close()
