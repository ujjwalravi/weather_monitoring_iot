from flask import render_template, jsonify
from app import app
from app.scripts import test_script, bolt_data

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/get_bolt_temp")
def get_bolt_temp():
	print("Hi Hello")
	res = bolt_data.get_temp()
	print (res)
	return jsonify(status = True, data = res), 200

@app.route("/get_rain_status")
def get_rain_status():
	res = bolt_data.get_rain_status()
	return jsonify(status = True, data = res), 200

@app.route("/test")
def test():
	test_script.execute()
	return "<h1>Test Route</h1>"