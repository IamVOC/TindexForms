from marshmallow import Schema, fields

class ContentObject(Schema):
    name = fields.String(required=True)
    field_type = fields.Number(required=True)
    field = fields.List(fields.String, required=True)

class FormObject(Schema):
    _id = fields.Number(required=True)
    name = fields.String(required=True)
    author_id = fields.Number(required=True)
    content = fields.List(fields.Nested(ContentObject, required=True), required=True)
    hook = fields.String(required=True)

class GetObject(Schema):
    _id = fields.Number(required=True)

