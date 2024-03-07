from flask import Flask, render_template, request, flash, redirect, url_for
import random
import string
import pyperclip

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            if length <= 0:
                flash('Password length must be a positive integer.', 'error')
                return redirect(url_for('index'))
        except ValueError:
            flash('Invalid input for password length.', 'error')
            return redirect(url_for('index'))

        include_uppercase = request.form.get('uppercase')
        include_lowercase = request.form.get('lowercase')
        include_numbers = request.form.get('numbers')
        include_symbols = request.form.get('symbols')

        character_set = ''
        if include_uppercase:
            character_set += string.ascii_uppercase
        if include_lowercase:
            character_set += string.ascii_lowercase
        if include_numbers:
            character_set += string.digits
        if include_symbols:
            character_set += '!@#$%^&*()'

        if not character_set:
            flash('Please select at least one character set.', 'error')
            return redirect(url_for('index'))

        password = ''.join(random.choices(character_set, k=length))
        pyperclip.copy(password)

        flash('Password generated and copied to clipboard!', 'success')
        return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
