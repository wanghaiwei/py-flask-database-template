from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from application.handler import meals as meals_handler


class Category(FlaskForm):
    category = SelectField('餐点：', validators=[DataRequired()])
    submit = SubmitField('获取推荐')
