from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            DataRequired(message="Це поле обов'язкове"),
            Length(min=4, max=10, message="Ім'я має бути від 4 до 10 символів")
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Це поле обов'язкове"),
            Email(message="Введіть коректну пошту")
        ]
    )

    phone = StringField(
        "Phone",
        validators=[
            Regexp(r'^\+380\d{7}$', message="Формат: +380XXXXXXX")
        ]
    )

    subject = SelectField(
        "Subject",
        choices=[
            ("question", "Question"),
            ("feedback", "Feedback"),
            ("other", "Other")
        ],
        validators=[DataRequired()]
    )

    message = TextAreaField(
        "Message",
        validators=[
            DataRequired(message="Це поле обов'язкове"),
            Length(max=500, message="Повідомлення має бути до 500 символів")
        ]
    )

    submit = SubmitField("Send")

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(message="Це поле обов'язкове")]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Це поле обов'язкове"),
            Length(min=4, max=10, message="Пароль має бути від 4 до 10 символів")
        ]
    )

    remember = BooleanField("Remember me")

    submit = SubmitField("Sign In")
