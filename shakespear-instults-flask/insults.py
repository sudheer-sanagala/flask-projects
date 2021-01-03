from flask import Flask, render_template, jsonify, render_template_string, render_template
import random, datetime

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

"""
Generate a random insult
"""
@app.route("/random")
def insult_me():
    #list_a = ['artless','bawdy','beslubbering','bootless','churlish']
    #list_b = ['base-court','bat-fowling','beef-witted','beetle-headed','boil-brained']
    #list_c = ['apple-john','baggage','barnacle','bladder','boar-pig']

    list_a = []
    list_b = []
    list_c = []

    with open("data/insults.csv", "r") as f:
        for line in f:
            words = line.split(",")
            list_a.append(words[0].strip())
            list_b.append(words[1].strip())
            list_c.append(words[2].strip())

    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

    insult = 'Thou'+' '+word_a+' '+word_b+' '+word_c
    #return jsonify(insult)
    
    """Renders the about page."""
    return render_template(
        'insults.html',
        title='About',
        year=datetime.date.today(),
        message= insult
    )

"""
About page
"""
@app.route("/about")
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.date.today(),
        message='Your application description page.'
    )

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)