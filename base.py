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
        self.send_response(200)
        self.end_headers()
        img = read_image()
        self.wfile.write(img)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


