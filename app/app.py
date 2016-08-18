
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)





@app.route('/')
def show_all():
    # student Students
	con = sql.connect("studentss.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from students")

	rows = cur.fetchall();
	#return render_template("list.html", rows=rows)




	return render_template('ns.html', rows=rows)




@app.route('/new', methods=['GET', 'POST'])
def new():
	if request.method == 'POST':
		if not request.form['name'] or not request.form['city'] or 	not request.form['addr']or not request.form['pin']:
			flash('Please enter all the fields', 'error')
		else:

			student = models.Students(request.form['name'], request.form['city'],request.form['addr'], request.form['pin'])

			db.session.add(student)
			db.session.commit()
			flash('Record was successfully added')
			db.create_all()
			return redirect(url_for('show_all'))



	return render_template('new.html')


if __name__ == '__main__':



	app.run(debug=True)

