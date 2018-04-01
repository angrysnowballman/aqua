
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask, request, abort, jsonify


app = Flask(__name__)


data = {}


@app.route('/dictionary/<key>', methods=['GET'])
def get_from_dict(key):
    if key not in data:
        abort(400)
    return jsonify(data[key])

@app.route('/dictionary', methods=['POST'])
def post_to_dict():
    if not request.json:
        abort(400)
    elif all(('key' not in request.json, 'value' not in request.json)):
        abort(400)
    if request.json.get('key') in data:
        abort(409)
    data[request.json.get('key')] = request.json.get('value')

    return jsonify({'success': True})


@app.route('/dictionary', methods=['PUT'])
def update_key():
    if not request.json:
        abort(400)
    elif all(('key' not in request.json, 'value' not in request.json)):
        abort(400)
    if request.json.get('key') not in data:
        abort(404)
    data[request.json.get('key')] = request.json.get('value')

    return jsonify({'success': True})


@app.route('/dictionary/<key>', methods=['DELETE'])
def remove_value(key):
    if key not in data:
        return jsonify({'result': 'null', 'time': datetime.now().strftime("%Y-%m-%d %H:%M")}), 200
    else:
        value = data[key]
        del data[key]
        return jsonify({'result': value, 'time': datetime.now().strftime("%Y-%m-%d %H:%M")}), 200


if __name__ == '__main__':
    app.run(debug=True)