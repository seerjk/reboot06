from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    res = ''
    if user == 'admin' and pwd == 'admin':
        res = 'ok'
    else:
        res = 'no'
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
