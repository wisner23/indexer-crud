from app.common.indexer_factory import ElasticFactory
from elasticsearch import Elasticsearch


class ElasticProvider(object):

    def __init__(self, index_name, doc_type, index_mapping):
        self.index_name = index_name
        self.doc_type = doc_type
        self.index_mapping = index_mapping
        self.elastic_factory = ElasticFactory()
        self.instance = None

    def connection(self) -> Elasticsearch:
        if not self.instance:
            self.instance = self.elastic_factory.create()

        if not self.instance.indices.exists(self.index_name):
            self.instance.indices.create(index=self.index_name, body=self.index_mapping)

        return self.instance

    def create(self, payload) -> bool:
        return self.connection().index(index=self.index_name, body=payload, doc_type=self.doc_type)

    def delete(self, id):
        return self.connection().delete(index=self.index_name, doc_type=self.doc_type, id=id)

    def update(self, id, payload):
        return self.connection().update(doc_type=self.doc_type, index=self.index_name, body=payload, id=id)
