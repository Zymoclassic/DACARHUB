from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Prints the current working directory
print("Current Working Directory:", os.getcwd())

# Configure SQLite URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# SQL database user class model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # The DB table name
    __tablename__ = 'dacarhub_user_table'


with app.app_context():
    # Creates the table name in the flask application
    db.create_all()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Password and Confirm Password must match', 'danger')
        else:
            # this will hash the password before storing it
            hashed_password = generate_password_hash(password, method='sha256')
            # this will create the new user objeect in the DB
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('regist.html')


@app.route('/login')
def login():
    return 'login.html'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
