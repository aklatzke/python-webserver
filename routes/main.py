from data.stores.index import search, title

routes = {
    "/" : {
        "template": "index",

        "children" : {

            "search": {
                "template": "index",
                "store" : search,
                "children": {
                    "{param}": {
                        "template": "index",
                        "store" : search
                    }
                }
            },

            "title" : {
                "template": "index",
                "store": title,
                "children" : {
                    "{param}" : {
                        "template" : "index",
                        "store" : title
                    }
                }
            }
            
        }        
    },
}
