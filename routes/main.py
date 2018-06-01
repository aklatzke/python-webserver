import json
from data.stores.index import search, title
from data.actions.omdb import request
from routes.router import Router

router = Router()

router.add("/search/{param}", {
    "store": search,
    "actions": { request },
    "template" : "search"
})

router.add("/title/{param}", {
    "store" : title,
    "actions": { request },
    "template" : "title"
})

router.add("/api/search/{param}", {
    "store" : search,
    "actions": { request },
    "json": True
})

router.add("/api/title/{param}", {
    "store" : title,
    "actions": { request },
    "json" : True
})
