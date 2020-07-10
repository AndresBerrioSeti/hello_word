from flask import Flask, render_template

app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')


@app.route(r'/add')
def add_contact():
    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run()