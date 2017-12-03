from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/study/01')
def study01():
    return render_template('study01.html')

@app.route('/study/02')
def study02():
    return render_template('study02.html')

@app.route('/serious/01')
def serious01():
    return render_template('serious01.html')

@app.route('/serious/02')
def serious02():
    return render_template('serious02.html')

if __name__ == '__main__':
  app.run(debug=True)
