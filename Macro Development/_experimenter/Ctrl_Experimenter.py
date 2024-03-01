import xmlrpc.client
import time
import subprocess
from threading import Thread

IP_list = []

with open("IP_LIST.txt") as file:
    for line in file:
        IP_list.append( line.strip().split(": ")[1] )

Helm = xmlrpc.client.ServerProxy('http://'+ IP_list[0] +':4001')
Wpns = xmlrpc.client.ServerProxy('http://'+ IP_list[1] +':4002')
Engr = xmlrpc.client.ServerProxy('http://'+ IP_list[2] +':4003')

# Helm = xmlrpc.client.ServerProxy('http://10.250.126.79:4001')
# Wpns = xmlrpc.client.ServerProxy('http://10.250.126.66:4002')
# Engr = xmlrpc.client.ServerProxy('http://10.250.122.60:4003')
print("Console Starting...")
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

if __name__=='__main__':
    try:
        while True:
            time.sleep(3)
            answer = input(" Start Training:   1\n Start Recording:  2\n Start Artemis M1: 3\n Start Survey 1:   4\n Start M2:         5\n Start Survey 2:   6\n Start M3:         7\n Start Survey 3:   8\n Stop Recording:   9\n ID share:         0\n")
            if answer == '1':
                Thread(target = Helm.start_training()).start()
                Thread(target = Wpns.start_training()).start()
                Thread(target = Engr.start_training()).start()
            elif answer == '2':
                Thread(target = Helm.start_recording()).start()
                Thread(target = Wpns.start_recording()).start()
                Thread(target = Engr.start_recording()).start()
            elif answer == '3':
                subprocess.run(['python', 'Start_Artemis_M1_E.py'])
                Thread(target = Helm.start_artemis_m1()).start()
                Thread(target = Wpns.start_artemis_m1()).start()
                Thread(target = Engr.start_artemis_m1()).start()
            elif answer == '4':
                Thread(target = Helm.start_survey1()).start()
                Thread(target = Wpns.start_survey1()).start()
                Thread(target = Engr.start_survey1()).start()
                subprocess.run(['python', 'Take_Screenshot1_E.py'])
            elif answer == '5':
                Thread(target = Helm.start_m2()).start()
                Thread(target = Wpns.start_m2()).start()
                Thread(target = Engr.start_m2()).start()
                subprocess.run(['python', 'Start_M2_E.py'])
            elif answer == '6':
                Thread(target = Helm.start_survey2()).start()
                Thread(target = Wpns.start_survey2()).start()
                Thread(target = Engr.start_survey2()).start()
                subprocess.run(['python', 'Take_Screenshot2_E.py'])
            elif answer == '7':
                Thread(target = Helm.start_m3()).start()
                Thread(target = Wpns.start_m3()).start()
                Thread(target = Engr.start_m3()).start()
                subprocess.run(['python', 'Start_M3_E.py'])
            elif answer == '8':
                Thread(target = Helm.start_survey3()).start()
                Thread(target = Wpns.start_survey3()).start()
                Thread(target = Engr.start_survey3()).start()
                subprocess.run(['python', 'Take_Screenshot3_E.py'])
            elif answer == '9':
                Thread(target = Helm.stop_recording()).start()
                Thread(target = Wpns.stop_recording()).start()
                Thread(target = Engr.stop_recording()).start()
                subprocess.run(['python', 'Stop_Recording_E.py'])
            elif answer == '0':
                ID = input("Give ID: ")
                Helm.idShare(ID)

    except KeyboardInterrupt:
        print("Stopped Loop")
    except ConnectionRefusedError:
        print("Server Closed")
    except TimeoutError:
        print("Connection ERROR")