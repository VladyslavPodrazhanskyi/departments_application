from app import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'about!'
