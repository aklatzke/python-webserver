from response.requestHandler import RequestHandler
from utilities.templateFormatter import BlankFormatter

class TemplateHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'

    def find(self, name, data = {}):
        try:
            template_file = open('templates/{}.html'.format(name))
            self.contents = template_file
            self.setStatus(200)
            self.data = data
            return True
        except:
            self.setStatus(404)
            return False

    def getContents(self):
        contents = self.contents.read()
        fmt = BlankFormatter()
        contents = fmt.format(contents, **self.data)
        return contents

    def getType(self):
        return 'template'
        


