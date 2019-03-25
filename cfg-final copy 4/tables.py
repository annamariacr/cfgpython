from flask_table import Table, Col

class Results(Table):
	id = Col('Id', show=False)
	country = Col('country')
	deaths = Col('Death')
	region = Col('Region')