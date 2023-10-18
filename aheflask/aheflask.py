# AHE FLASK
from flask import Flask, render_template

from aheflask.code import credentials_string
from aheflask.code import AUTHOR_NAME

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/credentials',  methods=['GET'])
def credentials():
    return render_template('credentials.html', msg=credentials_string(AUTHOR_NAME))
