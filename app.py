from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Home/index.html")

@app.route("/registration")
def registration():
    return render_template("accounts/registration.html")

@app.route("/login")
def login():
    return render_template("accounts/Login.html")

@app.route("/account")
def account():
    return render_template("accounts/Account.html")

@app.route("/posts")
def posts():
    return render_template("Posts/Posts.html")

@app.route("/posts/create")
def create_post():
    return render_template("Posts/Create.html")

@app.route("/posts/update")
def update_post():
    return render_template("Posts/update.html")

@app.route("/security")
def security():
    return render_template("Security/security.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)