import flask, kssbmenu
from flask import render_template, request

m = kssbmenu.kssb_menu()
app = flask.Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/get_raw")
def get_menu():
	return m.download()

@app.route("/api/get")
def get():
	day = request.args.get("day")
	print(f"Request for day: {day}")
	tempmenu = m.download()
	if day == "" or day not in tempmenu: return "Wrong day"
	return str(tempmenu[day])

app.run()
