from flask import Flask, render_template
from flask.json import jsonify
from namegenerator import NameGenerator

app = Flask(__name__)
generator = NameGenerator('data')


@app.route("/")
def index():
    return render_template('index.html', name=generator.generate())


@app.route("/api/generate")
def generate():
    return jsonify(name=generator.generate())


@app.route("/api/generate/male")
def generate_male():
    return jsonify(name=generator.generate_male())


@app.route("/api/generate/female")
def generate_female():
    return jsonify(name=generator.generate_female())
