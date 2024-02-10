import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.multi(2,3))
print(s.add(2,3))
print(s.minus(5,2))
print(s.system.listMethods())


# while True:
#     pass



