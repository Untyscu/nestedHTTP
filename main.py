from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from modules import zipper
# from modules import executor
RECEIVER = ''

if __name__ == '__main__':
    
    class CustomHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            headers = self.headers
            url_parts = urlparse(self.path)
            # query_parameters = parse_qs(url_parts.query)
            query = headers['Host']+'?'+url_parts.query
            bquery = bytes(query,'utf-8')
            zipped_query = zipper.zipper(bquery, 'zip')
            unzipped_query = zipper.zipper(zipped_query, 'unzip')

            self.send_response(200)
            self.end_headers()
            self.wfile.write(unzipped_query)

        def do_POST(self):
            print()
    print()

    httpd = HTTPServer(('172.18.62.32', 8080), CustomHandler)
    httpd.serve_forever()