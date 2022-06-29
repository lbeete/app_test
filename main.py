from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify({"url": "hola"})
