from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/exec01', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        passwd = request.form.get('passwd')
        print name, passwd
        if name == 'admin' and passwd == 'admin':
            return "yes"
        else:
            return "no"
    return render_template('exec01.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
