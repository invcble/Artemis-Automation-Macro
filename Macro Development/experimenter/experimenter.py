import xmlrpc.client
import time
import subprocess

# party = xmlrpc.client.ServerProxy('http://10.250.8.83:4000')
party = xmlrpc.client.ServerProxy('http://localhost:4000')

# print(party.add(2,3))
# party.status()
print(party.system.listMethods())

try:
    while True:
        time.sleep(3)
        answer = input(" Start Training:   1\n Start Recording:  2\n Start Artemis M1: 3\n Start Survey 1:   4\n Start M2:         5\n Start Survey 2:   6\n Start M3:         7\n Start Survey 3:   8\n Stop Recording:   9\n")
        if answer == '1':
            party.actionOne()
            subprocess.run(['python', 'Macro Development\\experimenter\\test1.py'])
        elif answer == '2':
            party.actionTwo()
        else:
            ID = input("Give ID: ")
            party.idShare(ID)

except KeyboardInterrupt:
    print("Stopped Loop")
except ConnectionRefusedError:
    print("Server Closed")


