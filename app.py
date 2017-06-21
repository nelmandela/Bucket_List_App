from flask import Flask, render_template, request, redirect, url_for, flash
from classes.user import User

# Initialize the app
app = Flask(__name__, template_folder="UI/", static_folder="UI/", static_url_path="/static")
app.debug = True
app.secret_key = 'some_secret'
# prevent user index from being 0
users = [User('test', 'test', 'test')]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("sign_in.html")
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        check = user_exists(email)
        if check is False:
            flash("Wrong Username and/or Password")
            return render_template('sign_in.html')
        else:
            if users[check].login(password):
                return redirect(url_for('homepage'))
            else:
                flash("Wrong Username and/or Password")
                return render_template('sign_in.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('sign_up.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name, email, password)
        check = user_exists(email)
        if check is False:
            users.append(new_user)
            return redirect(url_for('login'))
        else:
            flash("Email Already Exists")
            return render_template("sign_up.html")

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")

def user_exists(email):
    for existing_user in users:
        if existing_user.email.lower() == email.lower():
            return users.index(existing_user)

    return False

if __name__ == '__main__':
    app.run()




