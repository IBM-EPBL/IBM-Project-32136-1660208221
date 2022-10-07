from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
        return "Hello"
@app.route("/user")
def demo():
        return "user logged in to python"
@app.route("/login")
def demoo():
        return render_template("Login.html") 

if __name__=="__main__":
        app.run(debug=True)
