from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		RA = request.form.get("RA")
		print(RA)


	return render_template('login.html')

app.run(host='0.0.0.0', port=8080)
