from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('homework1.html')

@app.route('/music')
def music():
    return '<h1>Music</h1>'

@app.route('/music/top100')
def music100():
    return '<h1>Music Top 100</h1>'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)