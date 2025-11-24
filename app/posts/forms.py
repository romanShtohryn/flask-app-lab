from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=150)])
    content = TextAreaField("Content", validators=[DataRequired()])
    category = SelectField("Category", choices=[
        ("news", "News"),
        ("publication", "Publication"),
        ("tech", "Tech"),
        ("other", "Other")
    ])
    is_active = BooleanField("Active")
    author = StringField("Author", default="Anonymous")
    submit = SubmitField("Save")
