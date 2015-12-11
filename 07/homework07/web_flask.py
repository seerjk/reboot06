# coding:utf-8

from flask import Flask, request, render_template, redirect
import db
# import use

app = Flask(__name__)

@app.route('/')
def index():
    res_tuple = db.select_all()
    error_info = request.args.get('error_info')
    return render_template('index.html', data=res_tuple, error=error_info)


@app.route('/add')
def add():
    name = request.args.get('name')
    passwd = request.args.get('passwd')

    if name == "":
        pass
        # error_info
    else:
        pass
        result_code = db.user_add(name, passwd)

    # url_for ?error_info=str
    return redirect('/')

@app.route('/delete')
def delete():
    # user = request.args.get('user')
    # if user in use.user_dict:
    #     use.user_dict.pop(user)
    #     use.update_file()
    #     return use.get_html()
    # else:
    #     return '<p>user no exist</p>' + use.get_html()
    pass


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9092)
