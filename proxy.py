#!/usr/bin/env python3
"""COTW Test Client Proxy — serves frontend + proxies API calls to COTW server."""
import http.server
import urllib.request
import json
import os
import time

COTW_BASE = os.environ.get("COTW_SERVER", "http://localhost:8080/COTW")

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            self.proxy_api()
        elif self.path == "/" or self.path == "":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()
    
    def proxy_api(self):
        url = f"{COTW_BASE}/{self.path[5:]}"  # /api/USER?action=... -> COTW/USER?action=...
        try:
            start = time.time()
            with urllib.request.urlopen(url, timeout=30) as resp:
                body = resp.read()
                elapsed = int((time.time() - start) * 1000)
                data = json.loads(body)
                data["_proxy_elapsed_ms"] = elapsed
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

PORT = int(os.environ.get("PORT", "9000"))
print(f"COTW Test Client → http://localhost:{PORT}")
print(f"Proxying to {COTW_BASE}")
http.server.HTTPServer(("0.0.0.0", PORT), ProxyHandler).serve_forever()
