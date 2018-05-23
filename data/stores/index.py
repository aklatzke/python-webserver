import http.client
import json

def omdbRequest(reqParam, params, page=1):
    request = http.client.HTTPConnection("omdbapi.com", 80)
    apikey = '6b112a2'
    requestUrl = "/?{}={}&page={}&apikey={}".format(reqParam, params['param'], page, apikey)
    print(requestUrl)
    request.request("GET", requestUrl)

    response = request.getresponse()
    responseContent = response.read()

    return responseContent

def search(params):
    currentPage = 1
    if "query" in params:
        currentPage = params["query"]["page"]

    responseContent = omdbRequest("s", params, currentPage)

    return {
        "response" : json.loads(responseContent)['Search'],
        "param" : params['param'],
        "title" : "Search Results",
        "pages" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "currentPage" : currentPage
    }

def title(params):
    if "param" not in params:
        return {
            "json": "",
            "param" : ""
        }

    responseContent = omdbRequest("i", params)

    return {
        "results": json.loads(responseContent),
        "param" : params['param']
    }
