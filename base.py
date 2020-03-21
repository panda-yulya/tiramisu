import http.server
import socketserver

PORT = 80

def read_image():
    i = None
    with open("C:\\Users\\yuliy\\Documents\\dev\\tiramisu\\iam.jpg", "rb") as f:
        i = f.read()
    return i    

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        #img = read_image()
        text = b"""<html>
        Hi, Pavel
        <img src="iam.jpg">
        </html>"""
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(text) 
        elif self.path == "/iam.jpg":
            self.send_response(200)
            self.end_headers()
            img = read_image()
            self.wfile.write(img)
        elif self.path == "/favicon.ico":
            self.send_response(200)
            self.end_headers()
            img = read_image()
            self.wfile.write(img)
        else:
            self.send_response(404)
            self.end_headers()
            print("stop")
            

        #print("request ok %s" % (self.path))
     

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


