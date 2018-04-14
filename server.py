import os

from routes.routeHandler import RouteHandler
from http.server import BaseHTTPRequestHandler
from response.templateHandler import TemplateHandler
from response.staticHandler import StaticHandler
from response.badRequestHandler import BadRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]

        if request_extension is "" or request_extension is ".html":
            route_handler = RouteHandler()

            if route_handler.find(self.path): 
                handler = TemplateHandler()
                route_result = route_handler.get_result()
                handler.find(route_result["template"], route_result["data"])
            else: 
                handler = BadRequestHandler()

        elif request_extension is ".py":
            handler = BadRequestHandler()

        else:
            handler = StaticHandler()
            handler.find(self.path)

        self.respond({
            'status': handler.getStatus(),
            'type': handler.getType(),
            'handler' : handler
        })

    def handle_http(self, status_code, handler):
        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"
        
        self.end_headers()

        if isinstance( content, (bytes, bytearray) ):
            return content

        return bytes(content, 'UTF-8')
        
    def respond(self, opts):
        response = self.handle_http(opts['status'], opts['handler'])
        self.wfile.write(response)
    

