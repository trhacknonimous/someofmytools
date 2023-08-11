from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    if 'authenticated' in session and session['authenticated']:
        with open('liste.json', 'r') as file:
            projects = json.load(file)
        return render_template('menu.html', projects=projects)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        allowed_passwords = os.environ.get('ALLOWED_PASSWORDS').split(',')
        if password in allowed_passwords:
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            return "Mot de passe incorrect"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')