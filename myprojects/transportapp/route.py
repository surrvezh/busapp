from transportapp import app
from flask import render_template
from transportapp.models import Item
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/tracker')
def tracker_page():
    items = Item.query.all()

    return render_template('tracker.html',items=items)

