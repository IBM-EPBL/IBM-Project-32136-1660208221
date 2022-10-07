from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
         return render_template("login.html")
@app.route("/Login" , methods=["POST"])
def Login():
    if request.method == "POST":
        user=request.form["name"]
         return render_template("login.html",y=user)
    if __name__==("__main__"):
        app.run(debug=True)
