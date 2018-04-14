from routes.main import routes
from functools import reduce

class RouteHandler():
    def find(self, route_name):
        route_parts = route_name.split("/")
        route_parts = [i if i else "/" for i in route_parts]

        self.result = self.find_route(routes, route_parts)
        if self.result:
            return True
        else:
            return False

    def get_result(self):
        return self.result

    def find_route(self, routes, route_parts, params = {}):
        new_params = {}
        routes["params"] = params

        for part in route_parts:
            last_part = False

            if part is route_parts[-1]:
                last_part = True

            for key in routes:
                if key in ("children", "params", "store"):
                    continue
                elif part in routes:
                    part = part
                elif( key.startswith("{") and key.endswith("}") ):
                    param_name = key.strip(r"{}")
                    new_params[param_name] = part
                    part = key

            if part in routes and last_part:
                this_route = routes[part]
                this_route["params"] = {**params, **new_params}

                if "store" in this_route:
                    this_route["data"] = this_route["store"]({ **params, **new_params })
                else:
                    this_route["data"] = {}

                return this_route
            elif part in routes and "children" in routes[part]:
                return self.find_route(routes[part]["children"], route_parts[1:], {**params, **new_params})
            elif part in routes: 
                this_route = routes[part]
                
                if "store" in this_route:
                    print(this_route)
                    this_route["data"] = this_route["store"]({**params, **new_params})
                else:
                    this_route["data"] = {}
                return this_route
            else:
                return False
        
        return False
            
