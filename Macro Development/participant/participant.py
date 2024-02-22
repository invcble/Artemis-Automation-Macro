from xmlrpc.server import SimpleXMLRPCServer
import time
import subprocess

# party = SimpleXMLRPCServer(('10.250.8.83', 4000))
party = SimpleXMLRPCServer(('localhost', 4000), allow_none=True)
party.register_introspection_functions()

def start_training():
    subprocess.run(['python', 'Macro Development/participant/test2.py'])

def actionTwo():
    print("HELLO, running test2.py")
    time.sleep(2)
    subprocess.run(['python', '\\Macro Development\\test2.py'])

def idShare(ID):
    print("Printing ID on server: "+ ID)

party.register_function(idShare)
party.register_function(actionOne)
party.register_function(actionTwo)
# server.handle_request()
# server.serve_forever()

try:
    party.serve_forever()
except KeyboardInterrupt:
    print("Stopped Server")