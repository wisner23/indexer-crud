from app.common.indexer_provider import ElasticProvider
from app.conf.imovel_mapping import imovel_mapping
from flask import Blueprint, request, abort
import json

mod_indexer = Blueprint("mod_indexer", __name__, url_prefix="/indexer")
elastic_provider = ElasticProvider("indexer-imovel", "imovel", imovel_mapping)


@mod_indexer.route("/", methods=["GET"])
def get_status():
    return "its working - crud"


@mod_indexer.route("/", methods=["POST"])
def create():
    if not request.json:
        abort(400)

    if not elastic_provider.create(request.json):
        return {"status_code": 500, "message": "Oops, an error occured, take a look in the log."}

    return json.dumps({})


@mod_indexer.route("/<id>", methods=["PUT"])
def update(id):
    if not request.json:
        abort(400)

    return elastic_provider.update(id, request.json)


@mod_indexer.route("/<id>", methods=["DELETE"])
def delete(id):
    return elastic_provider.delete(id)
