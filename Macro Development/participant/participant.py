from xmlrpc.server import SimpleXMLRPCServer
import time
import subprocess

party = SimpleXMLRPCServer(('10.250.114.28', 4000), allow_none=True)
# party = SimpleXMLRPCServer(('localhost', 4000), allow_none=True)
party.register_introspection_functions()

def start_training():
    subprocess.run(['python', 'Start_Training_P.py'])

def start_recording():
    subprocess.run(['python', 'Start_Recording_P.py'])

def start_artemis_m1():
    subprocess.run(['python', 'Start_Artemis_M1_P.py'])

def start_survey1():
    subprocess.run(['python', 'Start_Survey1_P.py'])

def start_m2():
    subprocess.run(['python', 'Start_M2_P.py'])

def start_survey2():
    subprocess.run(['python', 'Start_Survey2_P.py'])

def start_m3():
    subprocess.run(['python', 'Start_M3_P.py'])

def start_survey3():
    subprocess.run(['python', 'Start_Survey3_P.py'])

def stop_recording():
    subprocess.run(['python', 'Stop_Recording_P.py'])

def idShare(ID):
    print("Printing ID on server: "+ ID)


party.register_function(start_training)
party.register_function(start_recording)
party.register_function(start_artemis_m1)
party.register_function(start_survey1)
party.register_function(start_m2)
party.register_function(start_survey2)
party.register_function(start_m3)
party.register_function(start_survey3)
party.register_function(stop_recording)
party.register_function(idShare)


try:
    party.serve_forever()
except KeyboardInterrupt:
    print("Stopped Server")