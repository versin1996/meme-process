from flask import Flask, render_template, request
from flask import jsonify
from waitress import serve
import shutil
import json
import os
import sys

from app.view import index, manipulate, show, prev, save, getContent, modify, saveModification


app = Flask(__name__)
app.DEBUG=True
app.jinja_env.auto_reload = True

app.add_url_rule('/', 'index', index)
app.add_url_rule('/manipulate', 'manipulate', manipulate)
app.add_url_rule('/show', 'show', show)

app.add_url_rule('/prev', 'prev', prev, methods=['POST'])
app.add_url_rule('/save', 'save', save, methods=['POST'])
app.add_url_rule('/getContent', 'getContent', getContent, methods=['POST'])
app.add_url_rule('/modify', 'modify', modify, methods=['POST'])
app.add_url_rule('/saveModification', 'saveModification', saveModification, methods=['POST'])

if __name__ == '__main__':
    serve(app, port=5000)