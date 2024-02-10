import xmlrpc
from xmlrpc.server import SimpleXMLRPCServer

server =  SimpleXMLRPCServer(('localhost', 8000))
server.register_introspection_functions()

def add(x, y):
   return x + y

def multi(x,y):
    return x*y
    
def minus(x,y):
    return x-y

def client_func():
    try:
        client = xmlrpc.client.ServerProxy('http://localhost:8001')
        client.hello()
    except Exception:
        print("ERROR")

server.register_function(add)
server.register_function(multi)
server.register_function(minus)
server.register_function(client_func)

server.serve_forever()