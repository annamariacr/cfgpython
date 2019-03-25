from wtforms import Form, StringField, SelectField
 
class CrisisSearchForm(Form):
    choices = [('Country', 'Country')]
    select = SelectField('Search crises:', choices=choices)
    search = StringField('')

class CrisisForm(Form):
    crisis_type = [('Refugees', 'Refugees'),
                   ('Deaths', 'Deaths'),
                   ('Disease', 'Disease'),
                   ('Assistance', 'Assistance')
                   ]
    country = StringField('Country')
    region = StringField('Region')
    crisis_type = SelectField('Crisis', choices=crisis_type)