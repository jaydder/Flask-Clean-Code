from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class UpdateForm(FlaskForm):
    old_username = StringField('Old Username', validators=[DataRequired(),], render_kw={"placeholder": "Old Username"})
    new_username = StringField('New Username', validators=[DataRequired(),], render_kw={"placeholder": "New Username"})
    new_password = PasswordField('New Password', validators=[DataRequired()], render_kw={"placeholder": "New Password"})
    submit = SubmitField('Update')
