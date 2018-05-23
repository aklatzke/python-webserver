import json
from data.stores.index import search, title
from routes.router import Router

router = Router()

router.add("/search/{param}", {
    "store": search,
    "template" : "search"
})

router.add("/title/{param}", {
    "store" : title,
    "template" : "title"
})

router.add("/api/search/{param}", {
    "store" : search,
    "json": True
})

router.add("/api/title/{param}", {
    "store" : title,
    "json" : True
})