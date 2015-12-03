# coding:utf-8
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login')
def index():
    # return "<h1>hello world</h1>"
    # return '<input type="button" value="click me">'
    # default dir: ./templates
    return render_template("login.html")


@app.route('/reboot')
def reboot():
    return "<h1>hello, reboot</h1>"


@app.route('/test1')
def test1():
    age = request.args.get('age')
    print age
    return "<h2>ages: %s</h2>" % age


@app.route('/test_form')
def test_form():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    res = ""
    if name == "jiangk":
        if passwd == "12345":
            res = "Welcome %s" % name
        else:
            res = "passord wrong."
    else:
        res = "%s doesn't exist." % name

    return res

# 
try:
    with open('user.txt') as f:
        lines = f.readlines()
except Exception, e:
    print "Error"
    exit(-1)

user_dict = {}

for line in lines:
    line = line.strip().split(' ')
    user_dict[line[0]] = line[1]


@app.route('/test_user_file')
def test_user_file():
    global user_dict
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    res = ""
    if name in user_dict:
        if passwd == user_dict[name]:
            res = "Welcome %s" % name
        else:
            res = "passord wrong."
    else:
        res = "%s doesn't exist." % name

    return res


@app.route('/table1')
def table1():
    return render_template("table1.html")

@app.route('/print_table')
def print_table():
    res = '''
    <table border="1">
        <thead>
            <tr>
                <th>name</th>
                <th>passwd</th>
            </tr>
        </thead>
        <tbody>
    '''
    for name, pwd in user_dict.items():
        res += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' % (name, pwd)

    res += '''
        </tbody>
    </table>
    '''
    return res


@app.route('/user_table')
def user_table():
    res = '''
    <table border="1">
        <thead>
            <tr>
                <th>姓名</th>
                <th>密码</th>
                <th>操作</th>
            </tr>
        </thead>
        <tbody>
    '''
    for name, pwd in user_dict.items():
        res += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' % (name, pwd)

    res += '''
        </tbody>
    </table>
    '''
    return res

@app.route('/test_args')
def test_args():
    name = request.args.get('name')
    print "len: %d, name: (%s), type: %s" %( len(name), name, type(name))
    return "len: %d, name: (%s), type: %s" %( len(name), name, type(name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002, debug=True)
