import os, http.server, socketserver
port = int(os.environ.get('PORT', 3456))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', port), handler) as httpd:
    print(f'Serving on port {port}')
    httpd.serve_forever()
