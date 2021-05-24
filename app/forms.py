from wtforms import Form, StringField, SubmitField, validators


class ProductForm(Form):
    productId = StringField(
        'Enter product Id',
        [
            validators.DataRequired(message="Product ID id needed"),
            validators.Length(
                min=8, max=8, message="Product Id must be 8 characters long"),
            validators.Regexp(
                regex="^[0-9]+$", message="Digits only")
        ])
    submit = SubmitField('Extract')
