import http.server, socketserver, urllib.request, json

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            ip = urllib.request.urlopen("https://api.ipify.org", timeout=8).read().decode()
        except Exception as e:
            ip = f"ERROR: {e}"
        body = json.dumps({"egress_ip": ip}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass

with socketserver.TCPServer(("0.0.0.0", 8080), H) as httpd:
    httpd.serve_forever()
