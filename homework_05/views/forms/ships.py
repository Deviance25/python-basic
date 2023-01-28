from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreateProductForm(FlaskForm):
    name = StringField(
        label="Ship name",
        name="ship-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        # render_kw={'class': 'form-control'}
    )