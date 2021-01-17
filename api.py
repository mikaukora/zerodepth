import flask
from flask import request, jsonify
from calc import calc

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def home():
    data = request.json
    depths = calc.calculate_depth(data)
    return jsonify(depths)

app.run()
