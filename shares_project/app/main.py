from . import app

@app.route('/main')
def main():
    return "main"
