from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['!', '+', '@', '#', '$', '%', '&']

    x = int(request.form['num_alpha'])
    y = int(request.form['num_num'])
    z = int(request.form['num_symbols'])

    password = ""

    for _ in range(x):
        password += random.choice(alpha)

    for _ in range(y):
        password += random.choice(num)

    for _ in range(z):
        password += random.choice(symbol)

    pass_list = list(password)
    random.shuffle(pass_list)
    password = ''.join(pass_list)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
