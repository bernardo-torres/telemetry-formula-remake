
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
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.PORT = 8078
        self.exitFlag = 0
        self.isRunning = False

    def setData(self,Data):
        self.Handler = getHandler(Data)
        
    def run(self):
        self.resume()
        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            httpd.timeout = 5
            while self.exitFlag == 0:
                if self.isRunning:
                    httpd.handle_request()
            
    def pause(self):
        self.isRunning = False

    def resume(self):
        print("serving at port", self.PORT)
        self.isRunning = True
        
    def stop(self):
        threading.stop()
    