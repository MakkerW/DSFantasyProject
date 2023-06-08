from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

from GreenGroceries.queries import get_user_by_user_name, get_farmer_by_pk, get_customer_by_pk
from GreenGroceries.utils.choices import GWChoices,PositionChoices \

Gameweeks= GWChoices.choices()
last_element = Gameweeks[-1]  # Get the last element of the list
rest_of_list = Gameweeks[:-1]  # Get the rest of the list excluding the last element
GameweeksNew = [last_element] + rest_of_list
class FilterProduceForm(FlaskForm):
    full_name = StringField('Name')
    GW = SelectField('Gameweek',
                     validators=[DataRequired()],
                     choices=GameweeksNew)
    total_points = FloatField('FPL points')
    goals_scored = FloatField('Minimum goals scored')
    assists = FloatField('Minimum assists')
    price = FloatField('Price (lower than or equal to)',
                       validators=[NumberRange(min=0, max=100)])

    submit = SubmitField('Filter')



