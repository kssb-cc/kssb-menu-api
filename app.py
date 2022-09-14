import flask, kssbmenu
from flask import render_template, request

app = flask.Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/get_raw")
def get_menu():
	m = kssbmenu.kssb_menu()
	return m.download()


app.run()
