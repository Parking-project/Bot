from marshmallow import fields, Schema

class SPage(Schema):
    page_index = fields.Integer()
    page_size = fields.Integer()
