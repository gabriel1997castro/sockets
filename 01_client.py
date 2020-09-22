import http.client

def HTTPclient(host, port=None):
  L=int(input())
  for i in range(L):
    content=input()
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", content)
    resp = connection.getresponse()
    data = resp.read().decode()
    print(data)


HTTPclient('localhost', '3333')