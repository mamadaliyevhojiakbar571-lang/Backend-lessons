from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    foydalanuvchilar = ["Xojiakbar", "Akmal", "Sardor"]
    vazifalar = ["Kitob o'qish", "Misol yechish"]

    def javob_ber(self, status, matn):
        self.send_response(status)
        self.send_header('Content-Type', 'text/plain; charset=utf-8' )
        self.end_headers()
        self.wfile.write(matn.encode())

    def do_GET(self):
        if self.path == '/users':
            self.javob_ber(200, f"Foydalanuvchilar {self.foydalanuvchilar}")
        elif self.path == '/tasks':
            self.javob_ber(200, f"Vazifalar {self.vazifalar}")
        else:
            self.javob_ber(404, "Topilmadi")

HTTPServer(('',8000),Handler).serve_forever()

