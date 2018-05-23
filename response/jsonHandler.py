from response.requestHandler import RequestHandler
import json

class JsonHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'application/json'
        self.setStatus(200)

    def format(self, data):
        self.contents = json.dumps(data)

    def getContents(self):
        return self.contents

    def getType(self):
        return 'template'
        


