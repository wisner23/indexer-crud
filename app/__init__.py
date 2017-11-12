from flask import Flask
from app.mod_indexer.api import mod_indexer

app = Flask(__name__)
app.register_blueprint(mod_indexer)
