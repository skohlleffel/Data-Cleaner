from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class RemoveEmail(FlaskForm):
    partners = StringField('Add emails or emails of partners to remove ', validators=[DataRequired()])
