# coding:utf-8

from flask import Flask, request, render_template, redirect, url_for
import db
# import use

app = Flask(__name__)

@app.route('/')
def index():
    res_tuple = db.select_all()
    error_info = request.args.get('error_info')
    # print error_info
    return render_template('index.html', data=res_tuple, error=error_info)


@app.route('/add')
def add():
    name = request.args.get('name')
    passwd = request.args.get('passwd')
    error_info = ""

    if name == "" or passwd == "":
        error_info = "name or password is empty."
    else:
        result_code = db.user_add(name, passwd)
        if result_code == -1:
            error_info = "db error!"
        elif result_code == 0:
            error_info = "changed %s's password." % name
        else:
            # 1
            error_info= "add a new user."

    # url_for ?error_info=str
    red_url = url_for('index', error_info=error_info)
    # print "*********************"
    # print red_url
    # return redirect("/?error_info=%s" % (error_info))
    return redirect(red_url)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    error_info = ""

    result_code = db.user_delete_by_id(id)
    if result_code == 0:
        error_info = "id not exist"

    return redirect("/?error_info=%s" % (error_info))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9092)
