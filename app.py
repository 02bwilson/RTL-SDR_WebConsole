from flask import render_template, Flask
from

app = Flask(__name__)

SDR_Controller = SDRController()


@app.route('/')
def index():
    return render_template('index.html')