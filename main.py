try:
    from flask import Flask, render_template, jsonify
except:
    import os
    os.system('pip install flask')
#holajaas

from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='Templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def rest():
    return jsonify({"xd": "hola"})

if __name__ == '__main__':
    print('Done!')
    app.run()
