#!/usr/bin/env python3

from flask import Flask

SECRET_MSG = "fluffy tail"
app = Flask(__name__)

@app.route('/')
def get_secret_message():
    return SECRET_MSG