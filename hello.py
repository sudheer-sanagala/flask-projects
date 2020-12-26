from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/check")
def check():
    return f"OK, the server is up and running."

@app.route("/hello/<string:name>")
def hello(name):
    return render_template('test.html',name=name)

@app.route("/dict")
def return_dict():
    """
    Returns a dictionary
    """
    return {"Key":"Value"}
    pass

if __name__ == "__main__":
    app.run(debug=True)