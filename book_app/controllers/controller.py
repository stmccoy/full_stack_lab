from app import app
from flask import render_template, request

@app.route('/')
def index():
    return "Hello World"