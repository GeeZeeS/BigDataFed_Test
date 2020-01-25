from flask import Flask, json, jsonify, url_for, render_template, request
import requests
import os

from xlsx_parser.xlsx_parser import load_json

app = Flask(__name__)
data = []


@app.route('/')
def hello():
    return jsonify(data)


@app.route('/data')
def data():
    week_start = request.args.get('week_start')
    week_end = request.args.get('week_end')
    if week_start and week_end:
        for filter_data in data:
            if filter_data['week_end'] == week_end and \
                    filter_data['week_start'] == week_start:
                return jsonify(filter_data)
        return jsonify({'error': '404 not found'})
    else:
        return jsonify({'error': 'week_start or week_end value incorect'})


if __name__ == '__main__':
    data = load_json(data)
    app.run(debug=True, port='8080')
