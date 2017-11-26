from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     return 'Hello C4E13'
#
# @app.route('/hello-me')
# def hello_me():
#     return 'Hello meo'
#
# @app.route('/<lastname>/<firstname>')
# def hello(lastname, firstname):
#     return "Hello " + lastname + ' ' + firstname
#
# @app.route('/sum/<int:x>/<int:y>')
# def sum(x, y):
#     a = str(x + y)
#     return str(x) + ' + ' + str(y) + ' = ' + a

if __name__ == '__main__':
  app.run(debug=True)
