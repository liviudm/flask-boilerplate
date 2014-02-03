from flask import render_template, url_for
from app import app

# create your views here (controller code)

@app.route('/')
def index():
    return render_template('index.html')

