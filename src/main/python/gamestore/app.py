import os

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gamestore.db')

db = SQLAlchemy(app)


class Game(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

    def __str__(self):
        return "Title: {self.title}"


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        try:
            game = Game(title=request.form.get("title"))
            db.session.add(game)
            db.session.commit()
        except Exception as e:
            print("Failed to add game")
            print(e)

    games = Game.query.all()
    return render_template("home.html", games=games)


@app.route('/update', methods=["POST"])
def update():
    try:
        new_title = request.form.get("newtitle")
        old_title = request.form.get("oldtitle")
        game = Game.query.filter_by(title=old_title).first()
        game.title = new_title
        db.session.commit()
    except Exception as e:
        print("Couldn't update game title")
        print(e)

    return redirect("/")


@app.route('/delete', methods=["POST"])
def delete():
    title = request.form.get("title")
    game = Game.query.filter_by(title=title).first()

    db.session.delete(game)
    db.session.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
