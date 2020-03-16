import http.server
import socketserver

PORT = 80


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        img = None
        with open("C:\\Users\\yuliy\\Documents\\dev\\tiramisu\\iam.jpg", "rb") as f:
            img = f.read()
        self.wfile.write(img)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


