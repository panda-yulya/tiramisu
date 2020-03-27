import http.server
import socketserver
import os

PORT = 80

program_dir = os.path.dirname(os.path.realpath(__file__))

def read_image(image_name):
    i = None
    image_path = os.path.join(program_dir, image_name)
    with open(image_path, "rb") as f:
        i = f.read()
    return i    


def read_text_file():
    t = None
    text_path = os.path.join(program_dir, "main_page.html")
    with open(text_path, "rt") as f:
        t = f.read()
    return t.encode()  

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            text = read_text_file()
            self.wfile.write(text) 
        elif self.path == "/iam.jpg":
            self.send_response(200)
            self.end_headers()
            img = read_image("iam.jpg")
            self.wfile.write(img)
        elif self.path == "/iam_1.jpg":
            self.send_response(200)
            self.end_headers()
            img = read_image("iam_1.jpg")
            self.wfile.write(img)
        elif self.path == "/favicon.ico":
            self.send_response(200)
            self.end_headers()
            img = read_image("iam.jpg")
            self.wfile.write(img)
        else:
            self.send_response(404)
            self.end_headers()
            print("stop")
            

        #print("request ok %s" % (self.path))
     

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


