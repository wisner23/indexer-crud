import os
from elasticsearch import Elasticsearch


class ElasticFactory(object):

    def __init__(self):
        self.host = os.environ["ELASTICSEARCH_HOST"]

    def create(self):
        return Elasticsearch(self.host)
