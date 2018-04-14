import http.client
import json

def omdbRequest(reqParam, params):
    request = http.client.HTTPConnection("omdbapi.com", 80)
    apikey = '6b112a2'
    request.request(
        "GET", "/?{}={}&apikey={}".format(reqParam, params['param'], apikey))

    response = request.getresponse()
    responseContent = response.read()

    return responseContent

def search(params):
    responseContent = omdbRequest("s", params)

    return {
        "json": str(json.dumps(json.loads(responseContent), sort_keys=True, indent=4)),
        "param" : params['param']
    }


def title(params):
    responseContent = omdbRequest("t", params)

    return {
        "json": str(json.dumps(json.loads(responseContent), sort_keys=True, indent=4)),
        "param" : params['param']
    }
