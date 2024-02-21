import xmlrpc.client
import time

# party = xmlrpc.client.ServerProxy('http://10.250.8.83:4000')
party = xmlrpc.client.ServerProxy('http://localhost:4000')

# print(party.add(2,3))
# party.status()
print(party.system.listMethods())

try:
    while True:
        time.sleep(3)
        answer = input("Console: 1,2,3\n")
        if answer == '1':
            party.actionOne()
        elif answer == '2':
            party.actionTwo()
        else:
            ID = input("Give ID: ")
            party.idShare(ID)

except KeyboardInterrupt:
    print("Stopped Loop")
except ConnectionRefusedError:
    print("Server Closed")


