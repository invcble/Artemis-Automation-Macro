from xmlrpc.server import SimpleXMLRPCServer
import time

server = SimpleXMLRPCServer(('10.250.8.83', 4000))
server.register_introspection_functions()
text = "hello"

def status():
    return text

def add(x, y):
    return x + y

def multi(x, y):
    return x * y

def minus(x, y):
    return x - y

server.register_function(add)
server.register_function(multi)
server.register_function(minus)
server.register_function(status)
server.handle_request()
# server.serve_forever()

while True:
    time.sleep(10)
    text = input("enter the command:\n")
    server.handle_request()