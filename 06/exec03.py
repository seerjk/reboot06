from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    lines = []

    try:
        with open('user.txt') as f:
            lines = f.readlines()
    except:
        return -1

    res = "<table border='1'>"
    res += '''
    <tr>
        <td>user</td>
        <td>password</td>
    </tr>
    '''
    for line in lines:
        # end with \n
        line = line.strip()
        name = line.split(' ')[0]
        passwd = line.split(' ')[1]
        res += '''
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
        ''' %(name, passwd)

    res += "</table>"
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
