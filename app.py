import json
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = "1.0"


def health():
    return {"status": "ok", "version": VERSION}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(health()).encode()
        self.send_response(200 if self.path == "/health" else 404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
