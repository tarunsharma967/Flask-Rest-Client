from flask import Flask, render_template, url_for, request,redirect
import services

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World<h1>'

@app.route('/all') 
def all():
	js = services.getAll()
	return render_template("list.html",js=js)

@app.route('/save', methods=['POST'])
def save():
	title = request.form['title']
	content = request.form['content']
	data = {'title':title, 
	'content':content}
	id = services.saveNote(data)
	return redirect(url_for('all'))

@app.route('/delete/<string:id>')
def delete(id):
	res = services.deleteNote(id)
	return redirect(url_for('all'))




app.run(debug= True, port=8000);
