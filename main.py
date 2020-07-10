from flask import Flask, render_template, request
from contact_model import Contact

app = Flask(__name__)


@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.from:
        contact = =Contact(name=request.from.get('name'), request.from.get('phone'), request.from.get('email'))
        
        contact.put()

    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run()