imovel_mapping = {
    "settings": {
        "number_of_shards": 3,
        "number_of_replicas": 2
    },
    "imovel": {
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "description": { "type": "string"},
            "price": {"type": "integer"},
            "coordinates": {"type": "geo_point"},
            "area": {
                "id": {"type": "string"},
                "name": {"type": "keyword"},
                "coordinates": {"type": "geo_point"},
                "country": {"type": "keyword"},
                "city": {"type": "keyword"}
            },
            "images": [{
                "url": { "type": "string"}
            }]
        }
    }
}