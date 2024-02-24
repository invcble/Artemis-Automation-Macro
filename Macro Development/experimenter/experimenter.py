import xmlrpc.client
import time
import subprocess

party = xmlrpc.client.ServerProxy('http://10.250.114.28:4000')
# party = xmlrpc.client.ServerProxy('http://localhost:4000')

#  Start Training:   1
#  Start Recording:  2
#  Start Artemis M1: 3
#  Start Survey 1:   4
#  Start M2:         5
#  Start Survey 2:   6
#  Start M3:         7
#  Start Survey 3:   8
#  Stop Recording:   9
#  ID share:         0
# print(party.system.listMethods())

try:
    while True:
        time.sleep(3)
        answer = input(" Start Training:   1\n Start Recording:  2\n Start Artemis M1: 3\n Start Survey 1:   4\n Start M2:         5\n Start Survey 2:   6\n Start M3:         7\n Start Survey 3:   8\n Stop Recording:   9\n ID share:         0\n")
        if answer == '1':
            party.start_training()
        elif answer == '2':
            party.start_recording()
        elif answer == '3':
            subprocess.run(['python', 'Start_Artemis_M1_E.py'])
            party.start_artemis_m1()
        elif answer == '4':
            party.start_survey1()
            subprocess.run(['python', 'Take_Screenshot1_E.py'])
        elif answer == '5':
            party.start_m2()
            subprocess.run(['python', 'Start_M2_E.py'])
        elif answer == '6':
            party.start_survey2()
            subprocess.run(['python', 'Take_Screenshot2_E.py'])
        elif answer == '7':
            party.start_m3()
            subprocess.run(['python', 'Start_M3_E.py'])
        elif answer == '8':
            party.start_survey3()
            subprocess.run(['python', 'Take_Screenshot3_E.py'])
        elif answer == '9':
            party.stop_recording()
            subprocess.run(['python', 'Stop_Recording_E.py'])
        elif answer == '0':
            ID = input("Give ID: ")
            party.idShare(ID)

except KeyboardInterrupt:
    print("Stopped Loop")
except ConnectionRefusedError:
    print("Server Closed")


