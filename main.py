from flask import Flask, render_template, request
from google.cloud import ndb
from contact_model import Contact

app = Flask(__name__)
client = ndb.Client()


@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html', contacts=contacts)


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.from:
        with client.context():
            contact = Contact(name=request.form.get('name'), request.form.get('phone'), request.form.get('email'))
            contact.put()

    return render_template('add_contact.html')

if __name__ == '__main__':
    app.run()