from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
        return render_template("index.html",title="Home Page")
@app.route("/Admin")
def Admin():
        return render_template("Admin.html",title="LOGIN")
@app.route("/User")
def User():
        return render_template("User.html",title="LOGIN")
@app.route("/Detail")
def Detail():
        return  render_template("Detail.html",title="Detail")
if __name__=="__main__":
        app.run(debug=True)
