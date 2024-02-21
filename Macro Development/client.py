import xmlrpc.client
import time

# s = xmlrpc.client.ServerProxy('http://10.250.8.83:4000')
s = xmlrpc.client.ServerProxy('http://localhost:4000')
print(s.multi(2,3))
print(s.add(2,3))
print(s.minus(5,2))
print(s.system.listMethods())

# while True:
#     time.sleep(3)
#     print(s.status())
    # pass



