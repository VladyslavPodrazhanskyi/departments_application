from src import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'about!'

@app.route('/contacts')
def contacts():
    return 'contact!'
