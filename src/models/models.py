from mongoengine import Document, StringField


class Link(Document):
    scheme = StringField(required=True)
    netloc = StringField(required=True)
    path = StringField()
    params = StringField()
    query = StringField()
    fragment = StringField()


