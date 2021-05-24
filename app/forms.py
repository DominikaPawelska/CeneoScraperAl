from wtforms import Form, BooleanField, StringField


class ProductForm(Form):
    productId = StringField(
        "Enter Product ID",
        [validators.DataRequired(message="Pleas enter ProductID"),
            validators.Lenght(
                min=8, max=8, message="Product Id must chave 8 charachters")
            validators.Regexp(
                regex="^\\d$", message="Product Id consist only of digits")
         ])
    submit = SubmitField("Find Product")
