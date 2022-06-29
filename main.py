try:
    from flask import Flask, render_template, jsonify
except ModuleNotFoundError:
    import os
    os.system('pip install flask')
    from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='Templates')

#a

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def rest():
    return jsonify({"xd": "hola"})

if __name__ == '__main__':
    print('Done!')
    app.run()
