from flask import render_template, flash
import requests
from converter import app
from converter.forms import InputDataForms


@app.route('/', methods=['GET', 'POST'])
def home():
    forms = InputDataForms()
    if forms.validate_on_submit():
        #date = forms.date.data
        base = forms.base.data
        currency = forms.currency.data
        quantity = forms.quantity.data
        
        base_url = f'https://economia.awesomeapi.com.br/last/{base}-{currency}'
        
        data_change = f'{base}{currency}'
        response = requests.get(base_url)
        if (response.ok is False):
            flash(f'Error: {response.status_code}')
            flash(f"{response.json()['error']}")
        else:
            data = response.json()
            total = quantity*float(data[data_change]['bid'])
            flash("{} {} = {:.2f} {} Day of".format(quantity, base, total, currency))

    return render_template('home.html', form=forms)