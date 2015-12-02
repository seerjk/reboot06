from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return 'hello flask'
    # return '<input type="button" value="click me!!">'
    # return '<input type="text">'
    # return '<input type="password">'
    # return '<input type="date">'
    # return '<input type="color">'
    # return '<input type="checkbox">'
    return render_template('index.html')

# @app.route('/reboot')
@app.route('/reboot', methods=['GET'])
def reboot():
    # http://10.1.1.8:9092/reboot?name=abcb
    name = request.args.get('name')
    age = request.args.get('age')
    # print type(request.args)
    # print request.args
    # http://10.1.1.8:9092/reboot?name=abcb&age=15
    return 'hello reboot, name: %s, age: %s' % (name, age)

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
        line = line.strip()
        name = line.split(' ')[0]
        passwd = line.split(' ')[1]
        user_dict[name] = passwd

    if user in user_dict:
        if str(pwd) == user_dict[user]:
            res = "yes, Login."
        else:
            res = "password is wrong, %s, %s" % (pwd, user_dict[user])
    else:
        res = "user name not exist."
    # if user == 'admin' and pwd == 'admin':
    #     res = 'ok'
    # else:
    #     res = 'no'
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
