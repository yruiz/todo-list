from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# class to instaciate the List table
class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def homepage():
    """
    Queries all the entries in the List table and retuns them in task_list
    Args: None
    Returns:
        index.html: the website template for the todo list
        task_list:  the list of all task currently in the table
    """
    # quearies the table for task, and returns them
    task_list = List.query.all()
    return render_template("index.html", task_list=task_list)


@app.route("/add", methods=["POST"])
def add():
    """
    Adds a new task to the todo list updating the List table and the homepage.
    Args:
        None
    Returns:
        redirected to the homepage
    """
    title = request.form.get("title")
    new_task = List(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/update/<int:task_id>")
def update(task_id):
    """
    Updates the progress label next to the task, by default it is grey,
    when clicked it turns to green or vice-versa.
    Args:
        task id - which identifies the task in the List table
    returns:
        redirects to the hompage with the updated label color.
    """
    task = List.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for("homepage"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    """
    Deletes the talk form the page and the List table
    Args:
        task id - which identifies the task in the List table
    returns:
        redirects to the hompage with the updated label color.
    """
    task = List.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("homepage"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
