from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

movies = {1: 'Toy story', 2: 'The Raid', 3: 'Hero',
            4: 'Ip Man', 5: 'Kung Fu Panda'}

fruits = ['apples','banana','grapes','oranges','mango']

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

@app.route("/fruits")
def fruit_list():
    """
    docstring
    """
    return render_template('test.html',len = len(fruits),fruits=fruits)
    pass

@app.route("/fruits/<string:fruit>")
def get_fruit(fruit):
    return f'You selected {fruit}'


@app.route("/movies")
def get_movies():
    """
    docstring
    """
    return render_template('movies.html',movies=movies)
    pass


if __name__ == "__main__":
    app.run(debug=True)