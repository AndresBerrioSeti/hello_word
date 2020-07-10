from google.appengine.ext import ndb

class Contact(ndb.Model):
    name = ndb.stringProperty()
    phone = ndb.stringProperty()
    email = ndb.stringProperty()