from . import app

@app.route('/views')
def index():
    return "hello world"
