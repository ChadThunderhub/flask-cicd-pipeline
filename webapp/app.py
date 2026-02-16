# Tworzenie prostej aplikacji internetowej w Flask

from flask import Flask, render_template
import os

from webapp.code import FirstName, LastName, Mail
from webapp.code import FIRST_NAME, LAST_NAME, MAIL
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def home():
    return render_template('main.html', firstName=FirstName(FIRST_NAME), lastName=LastName(LAST_NAME), mail=Mail(MAIL))

@app.route('/main',  methods=['GET'])
def main():
    return render_template('main.html', firstName=FirstName(FIRST_NAME), lastName=LastName(LAST_NAME), mail=Mail(MAIL))

@app.route('/time',  methods=['GET'])
def time():
    local_time = datetime.now()
    server_time = datetime.now(timezone.utc)
    return render_template('time.html', local_time = local_time, server_time=server_time)

@app.route('/gallery',  methods=['GET'])
def gallery():
    image_folder = os.path.join(app.root_path, 'static', 'images')
    images = [img for img in os.listdir(image_folder) if img.endswith(('JPG', 'PNG'))]
    return render_template('gallery.html', images = images)