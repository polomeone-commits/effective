from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 200 ОК
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode('utf-8'))

def run():
    # Порт 8080
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Backend запущен на порту 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()