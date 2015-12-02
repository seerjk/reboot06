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
    lines = []
    user_dict = {}

    try:
        with open('user.txt') as f:
            lines = f.readlines()
    except:
        return -1

    for line in lines:
        # end with \n
        line = line.strip()
        name = line.split(' ')[0]
        passwd = line.split(' ')[1]
        # name = line.split()[0]
        # passwd = line.split()[1]
        user_dict[name] = passwd

    if user in user_dict:
        if str(pwd) == user_dict[user]:
            res = "yes, Login."
        else:
            res = "password is wrong."
    else:
        res = "user name not exist."
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
