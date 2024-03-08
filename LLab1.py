from flask import Flask, render_template, request


lab11 = Flask(__name__)

@lab11.route("/")
def home():
    return render_template('index.html')

@lab11.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operator = request.form['operator']

    if operator == 'addition':
        result = num1 + num2
    elif operator == 'subtraction':
        result = num1 - num2
    elif operator == 'multiplication':
        result = num1 * num2
    elif operator == 'division':
        result = num1 / num2
    else:
        result = 'Invalid operator'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    lab11.run(debug=True) ##To reload the page once have changes
