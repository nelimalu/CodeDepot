from flask import Flask, redirect, url_for, render_template, request, session
from pathlib import Path

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
@app.route("/index/")
def home():
	return render_template("index.html")


@app.route("/courses/")
def courses():
	return render_template("courses.html")


@app.route("/favourites/")
def favourites():
	return render_template("favourites.html")


@app.route("/about/")
def about():
	return render_template("about.html")


@app.route("/login/", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		username = request.form['usrnm']
		password = request.form['pswrd']
		session['user'] = [username, password]
		return render_template("index.html")
	else:
		if "user" in session:
			return redirect("index.html")
		return render_template("login.html")

@app.route('/logout')
def logout():
	session.pop("user", None)
	return render_template("login.html")


if __name__ == "__main__":
	app.run(debug=True)
