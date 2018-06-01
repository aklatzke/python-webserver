import json

def search(params, omdbRequest):
    currentPage = 1

    if "query" in params:
        if "page" in params["query"]:
            currentPage = params["query"]["page"]

    responseContent = omdbRequest("s", params, currentPage)

    return {
        "response" : json.loads(responseContent)['Search'],
        "param" : params['param'],
        "title" : "Search Results",
        "pages" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "currentPage" : currentPage
    }

def title(params, omdbRequest):
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
