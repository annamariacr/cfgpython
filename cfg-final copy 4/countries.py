import pandas as pd
#from rethinkdb import init_db, db_session
from flask import Flask, render_template, request
import requests
import tablib
import os
from forms import CrisisSearchForm, CrisisForm

app = Flask("MyApp")
dataset = tablib.Dataset()
with open(os.path.join(os.path.dirname(__file__), 'data.csv')) as f:
    dataset.csv = f.read()
#init.db()

@app.route("/", methods=["GET", "POST"])
def index():
		search = CrisisSearchForm(request.form)
		if request.method == "POST":
			return search_results(search)
		else:
			return render_template('countries.html', form=search)

@app.route("/search")
def print_out_country_data():
	data = dataset.html
	#form_data = pd.read_csv('data.csv')
	return render_template('index.html', data=data)
#return render_template("countrydata.html", country=crisis_name.title())
#  user input $country same as name and email address in our example 
##return render_template("countries.html", country=country.title()
@app.route('/results')
def search_results(search):
    form_data = pd.read_csv('data.csv')
    results = []
    search_string = search.data['search']

    if search_string:
            if search.data['select'] == 'Country':
              qry= db_session.query(Country, Crisis).filter(
                Country.id==Country.Crisis_id).filter(
                  Country.name.contains(search_string))
              results = [item[0] for item in qry.all()]
            elif search.data['select'] == 'Crisis':
              qry = db_session.query(Crisis).filter(
                Crisis.title.contains(search_string))
              results = qry.all()
    if search.data['search'] == '':
        qry = db_session.query(Crisis)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)
 
@app.route('/crisis', methods=['GET', 'POST'])
def new_crisis():
    """
    Add a new crisis
    """
    form = CrisisForm(request.form)
    return render_template('countrydata.html', form=form)

    if request.method == 'POST' and form.validate():
        country = crisis_name()
        save_changes(crisis, form, new=True)
        flash('Crisis Recorded')
        return redirect('/')

    return render_template('countries.html', form=form)


if __name__ == '"MyApp"':
    app.run()

app.run(debug = True)