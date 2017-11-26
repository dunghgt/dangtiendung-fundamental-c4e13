from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<x>/<y>')
def bmi(x, y):
    bmi  = float(x) / (float(y) ** 2)
    if bmi < 16:
        a = ("Severely underweight")
    elif bmi < 18.5:
        a = ("Underweight")
    elif bmi < 25:
        a = ("Normal")
    elif bmi < 30:
        a = ("Overweight")
    else:
        a = ("Obese")
    return (a)
if __name__ == '__main__':
  app.run(debug=True)
