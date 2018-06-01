import http.client

def request(reqParam, params, page=1):
    request = http.client.HTTPConnection("omdbapi.com", 80)
    apikey = '6b112a2'
    requestUrl = "/?{}={}&page={}&apikey={}".format(
        reqParam, params['param'], page, apikey)
    print(requestUrl)
    request.request("GET", requestUrl)

    response = request.getresponse()
    responseContent = response.read()

    return responseContent
