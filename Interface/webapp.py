
import http.server
import socketserver
import threading
import json


class CORSRequestHandler (http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        global v1,v2,v3,v4,v5,v6,v7,v8,v9,v0,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19
        v0=v0+0.1;v1=v1+1;v2=v2+1;v3=v3+1;v4=v4+1;v5=v5+1;v6=v6-1;v7=v7-1;v8=v8-1;v9=v9-1;v10=v10+2;v11=v11+3;v12=v12+0.125;v13=v13+0.03125;v14=v14+4;v15=v15+5;v16=v16+6;v17=v17+0.5;v18=v18+0.25;v19=v19+0.75;
        data = {"v0":v0,"v1":v1,"v2":v2,"v3":v3,"v4":v4,"v5":v5,"v6":v6,"v7":v7,"v8":v8,"v9":v9,"v10":v10, "v11":v11, "v12":v12, "v13":v13, "v14": v14, "v15": v5, "v16":v16, "v17":v17,"v18":v18, "v19":v19 }
        response = json.dumps(data)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str.encode(response))



class Web_App_Server (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.PORT = 8078
        self.Handler = CORSRequestHandler
        self.exitFlag = 0
    def run(self):
        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            httpd.timeout = 3
            print("serving at port", self.PORT)
            while self.exitFlag == 0:
                print("Entrou run " + str(threading.active_count()))
                httpd.handle_request()
    #
    # def stop(self):
    #     self.exitFlag = 1
    #
    # def resume(self):
    #     self.exitflag = 0
