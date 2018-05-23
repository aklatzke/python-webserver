import json

class Router():
    def __init__(self, initialRoutes = {}):
        self.routes = initialRoutes
    
    def add(self, routeName, opts):
        routeParts = routeName.split("/")
        currentNode = self.routes
        for item in routeParts:
            if item is "":
                item = "/"

            if item not in currentNode:
                currentNode[item] = {}
            
            if item is routeParts[-1]:
                currentNode[item] = { **currentNode[item], **opts }
            else:
                if "children" not in currentNode[item]:
                    currentNode[item]["children"] = {}

                currentNode = currentNode[item]["children"]

    def getRoutes(self):
        return self.routes
            
