
import http.server
import socketserver
import threading
import json

def getHandler(Data):
    class CORSRequestHandler (http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            http.server.SimpleHTTPRequestHandler.end_headers(self)

        def do_GET(self):
            response = json.dumps(Data.dic)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(str.encode(response))
    return CORSRequestHandler 


class Web_App_Server (threading.Thread):
    def __init__(self, threadID, Data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.PORT = 8078
        self.Handler = getHandler(Data)
        self.exitFlag = 0
    
    def run(self):
        self.exitFlag = 0
        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            httpd.timeout = 5
            print("serving at port", self.PORT)
            while self.exitFlag == 0:
                httpd.handle_request()
            threading.stop()
    
    def stop(self):
        self.exitFlag = 1
