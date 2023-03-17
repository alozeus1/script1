from flask import Flask

app = Flask(__name__)

@app.route('/words')
def words():
    return 'This is the words endpoint'

if __name__ == '_main_':
    app.run(host='127.0.0.1', port=8989)

app.debug = True
