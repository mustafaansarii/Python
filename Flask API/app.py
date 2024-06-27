from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(299), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def greet():
    # Create a new Todo instance
    new_todo = Todo(title="First todo", desc="Start investing in stock")
    db.session.add(new_todo)
    db.session.commit()
    return render_template('index.html')

@app.route('/show')
def show_todos():
    all_todos = Todo.query.all()
    print(all_todos)
    return render_template("index.html",all_todos=all_todos)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure that the database and tables are created
    app.run(debug=True)
