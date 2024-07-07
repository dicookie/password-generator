# Password Generator

This is a password generator web application built with Flask. It provides a user friendly interface to generate secure passwords.

## Features

- Generate passwords of varying length
- Copy generated password to clipboard

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Dependencies**: Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sophiecookie/password-generator.git
   cd password-generator
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the application:
   ```bash
   py app.py
2. Open your web browser and go to:
   ```bash
   http://127.0.0.1:5000
3. (Optional) To use HTTPS for local development:
   
   - Generate a self-signed certificate:
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
   ```
   - Modify `app.py` to use SSL:
   ```bash
   if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
   ```
   - Access your application securely at:
   ```bash
   https://127.0.0.1:5000

## Screenshot
![An example of a generated password](https://i.postimg.cc/2jqDy95z/ezgif-7-05fcf5488c.gif)
