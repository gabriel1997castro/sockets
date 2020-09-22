import http.client
import mimetypes

def HTTPclient(host, port):
    L = int(input())
    for i in range(L):
        content = input()
        connection = http.client.HTTPConnection(host, port)
        connection.request("GET", content)
        response = connection.getresponse()
        status = response.status
        headers = response.getheaders()
        if (status == 200):
            contentType = [item for item in headers if item[0] == 'Content-type'][0][1]
            if (contentType == 'text/html'):
                print('Browsing:', content)
            elif (contentType == 'application/json'):
                print('Processing JSON:', content)
            elif (contentType == 'video/x-msvideo'):
                print('Playing media:', content)
            elif (contentType == 'audio/mpeg'):
                print('Playing audio:', content)
            else:
                fileType = mimetypes.guess_type(content)[0]
                stringToPrint = 'Unknown file/media: ' + fileType + '-' + content
                print(stringToPrint)
        if (status == 404):
            print('Content not found')
            

HTTPclient('localhost', '3333')