from http.server import HTTPServer, BaseHTTPRequestHandler
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("Bu mening ikinchi serverim".encode())

HTTPServer(('', 8080), MyHandler).serve_forever()