import string

class TemplateFormatter(string.Formatter):
    def __init__(self, default='', templatePath="templates/partials/"):
        self.default = default
        self.templatePath = templatePath

    def get_value(self, key, args, kwds):
        if "each " in key:
            return self.format(self.handle_each(key, kwds), **kwds)
        elif ">" in key:
            return self.format(self.handle_partial(key), **kwds)
        elif isinstance(key, str):
            return kwds.get(key, self.default)
        else:
            return string.Formatter.get_value(key, args, kwds, {})

    def handle_partial(self, key):
        key = key.replace(">", "").replace(" ", "")
        contents = open((self.templatePath + "{}.html").format(key))
        return contents.read()

    def handle_each(self, key, kwds):
        key = key.replace("each", "").replace(" ", "", 1)
        split = key.split("=", 1)
        searchKey = split[0].strip()
        partialKey = split[1]

        if partialKey.strip()[0] is ">":
            partial = self.handle_partial(partialKey)
        else:
            partial = partialKey.replace("(", "{").replace(")", "}")
        
        values = kwds.get(searchKey, [])

        output = ""

        for i in values:
            if( isinstance(i, dict) ):
                output += self.format(partial, **i)
            else:
                value = {"value" : i}
                output += self.format(partial, **{**value, **kwds})
                
        return output
            
            
