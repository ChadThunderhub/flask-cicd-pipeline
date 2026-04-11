from flask import Flask, render_template
import os

from webapp.code import FIRST_NAME, LAST_NAME, MAIL
from datetime import datetime, timezone

app = Flask(__name__)

IMAGE_FOLDER = os.path.join(app.root_path, 'static', 'images')
if os.path.exists(IMAGE_FOLDER):
    CACHED_IMAGES = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith(('JPG', 'PNG', 'jpg', 'png'))]
else:
    CACHED_IMAGES = []

# def home():
#     return render_template('main.html', firstName=FirstName(FIRST_NAME), lastName=LastName(LAST_NAME), mail=Mail(MAIL))

@app.route('/',  methods=['GET'])
@app.route('/main',  methods=['GET'])
def main():
    return render_template('main.html', firstName=FIRST_NAME, lastName=LAST_NAME, mail=MAIL)

@app.route('/time',  methods=['GET'])
def time():
    local_time = datetime.now()
    server_time = datetime.now(timezone.utc)
    return render_template('time.html', local_time = local_time, server_time=server_time)

@app.route('/gallery',  methods=['GET'])
def gallery():
    return render_template('gallery.html', images=CACHED_IMAGES)