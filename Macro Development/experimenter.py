import xmlrpc.client
import time

# s = xmlrpc.client.ServerProxy('http://10.250.8.83:4000')
party = xmlrpc.client.ServerProxy('http://localhost:4000')

# print(party.add(2,3))
# party.status()
print(party.system.listMethods())

try:
    while True:
        time.sleep(3)
        party.name()
        # pass
except KeyboardInterrupt:
    print("Stopped Loop")
except ConnectionRefusedError:
    print("Server Closed")


