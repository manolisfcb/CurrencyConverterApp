from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, SubmitField
import requests

class InputDataForms(FlaskForm):
    url = 'https://economia.awesomeapi.com.br/json/available/uniq'
    response = requests.get(url)
    curr = response.json().keys()
    curr = list(curr)
    choice = []
    for i in curr:
        tpl = (i, i)
        choice.append(tpl)

    #date = DateField("Enter Date in This Format(yyyy-mm-dd) ")
    base = SelectField('base', choices=choice, default='BRL')
    currency = SelectField('currency', choices=choice, default='USD')
    quantity = FloatField(f'How Much Currency You Convert?')
    submit = SubmitField('Calculate')