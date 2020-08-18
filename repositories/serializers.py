from marshmallow import Schema, fields


class RepositorySchema(Schema):
    fullName = fields.String()
    description = fields.String()
    cloneUrl = fields.Url()
    stars = fields.Integer()
    createdAt = fields.DateTime(format="iso")


REPOSITORY_SCHEMA = RepositorySchema()
