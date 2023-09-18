from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from modules import request_handler
RECEIVER = ''

if __name__ == '__main__':
    
    class CustomHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            headers = self.headers
            url_parts = urlparse(self.path)
            query_parameters = parse_qs(url_parts.query)
            print(headers['Host']+'n\****\n')
            print(query_parameters)
        
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes('GET запит оброблено успішно.','utf-8'))

        def do_POST(self):
            print()
    print()

    httpd = HTTPServer(('172.18.62.32', 8080), CustomHandler)
    httpd.serve_forever()