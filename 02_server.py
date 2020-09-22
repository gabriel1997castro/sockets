import http.server
import socketserver
host = "localhost"
port = 3333


def HTTPserver(host, port):
    try:
        reqHandler = http.server.SimpleHTTPRequestHandler
        global httpd
        httpd = socketserver.TCPServer((host, port), reqHandler)
        # print("serving at port", port)

        httpd.serve_forever()
    except Exception as error:
        if httpd is not None:
            httpd.shutdown()
            httpd.server_close()
        # print('error: ', error)

HTTPserver(host, port)