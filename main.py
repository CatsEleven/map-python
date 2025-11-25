from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/link')
def index():
    return render_template('adult.html', name='Flask Beginner')

if __name__ == '__main__':
    app.run(debug=True)