from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/api')
def index():
    return jsonify({"url": "hola"})

if __name__ == '__main__':
    app.run(debug=True)
