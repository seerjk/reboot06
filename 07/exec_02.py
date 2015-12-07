# coding:utf-8
import db
import use
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    sql_str = "select * from server"
    res_tuple = db.execute(sql_str)
    return render_template('print_table.html', data=res_tuple)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9092)
