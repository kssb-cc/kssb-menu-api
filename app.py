import flask, kssbmenu, sys
from flask import render_template, request, jsonify

m = kssbmenu.kssb_menu()
app = flask.Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/get_raw")
def get_raw():
	return jsonify(m.download())

@app.route("/api/get")
def get():
	day = request.args.get("day")
	print(f"Request for day: {day}")
	tempmenu = m.download()
	if day == "" or day not in tempmenu: return "Wrong day"
	return str(tempmenu[day])

app.run(host = "0.0.0.0", port = (5300 if len(sys.argv) <2 else sys.argv[1]))
