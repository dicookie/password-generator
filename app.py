from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def generate_passowrd(length):
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def publish_password():
    length=int(request.form['length'])
    password = generate_passowrd(length)
    return render_template('index.html',password=password)

if __name__ == '__main__':
    app.run(debug=True)