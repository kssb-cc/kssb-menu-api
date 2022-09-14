import flask, kssbmenu
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/")
def home():
	return """
<h1>Error</h1>
<p>Unfortunately, it isn't possible to access this API this way.<br>
You can check out the <a href="https://kssb.net/parents/menus">KSSB Menu on the main site</a>, though.</p>
	"""


@app.route("/api/get_raw")
def get_menu():
	m = kssbmenu.kssb_menu()
	return m.download()


app.run()
