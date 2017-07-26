from flask import Flask, render_template, make_response
from flask.json import jsonify
from functools import wraps
from namegenerator import NameGenerator

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
generator = NameGenerator('data')


def no_cache(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        resp = make_response(fn(*args, **kwargs))
        resp.cache_control.no_cache = True
        return resp
    return wrapped


@app.route("/")
@no_cache
def index():
    return render_template('index.html', name=generator.generate())


@app.route("/api/generate")
@no_cache
def generate():
    return jsonify(name=generator.generate())


@app.route("/api/generate/male")
@no_cache
def generate_male():
    return jsonify(name=generator.generate_male())


@app.route("/api/generate/female")
@no_cache
def generate_female():
    return jsonify(name=generator.generate_female())
