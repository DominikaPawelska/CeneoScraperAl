from wtforms import StringField, SubmitField, validators
from flask_wtf import FlaskForm


class ProductForm(FlaskForm):
    productId = StringField(
        'Enter product Id',
        [
            validators.DataRequired(message="ID must be given"),
            validators.Length(
                min=8, max=10, message="Product Id must have at least  8 characters"),
            validators.Regexp(
                regex="^[0-9]+$", message="id contains only digits ")
        ])
    submit = SubmitField('Extract')
