import socket
import http.client

socket.setdefaulttimeout(23)

# HOST = '127.0.0.1'
# PORT = 65432

url = 'http://google.com/'

try:
    a = http.client.HTTPConnection(url)
    a.connect()
except http.client.HTTPException as e:
    print('Connectivity failed: ')
    print(str(e))
