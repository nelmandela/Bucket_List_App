from flask import Flask, render_template, request, redirect, url_for, flash
from classes.user import User
from classes.bucketlist import BucketList

# Initialize the app
app = Flask(__name__, template_folder="UI/", static_folder="UI/", static_url_path="/static")
app.debug = True
app.secret_key = 'some_secret'
# prevent user index from being 0
# users = [User('test', 'test', 'test')]
check = -1

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("sign_in.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        check = user_exists(email)
        if check == -1:
            flash("Wrong Username and/or Password")
            return render_template('sign_in.html')
        else:
            if User.users[check].login(password):
                user = User.users[check]
                return render_template('homepage.html',
                                       user=user.name,
                                       buckets=user.bucketlists)
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
        check = user_exists(email)
        if check == -1:
            new_user = User(name, email, password)
            User.users.append(new_user)
            return redirect(url_for('login'))
        else:
            flash("Email Already Exists")
            return render_template("sign_up.html")
 
@app.route('/bucketlist', methods=['GET', 'POST'])
def bucketlist(id = None):
    if request.method == 'GET':
        return redirect(url_for('homepage'))
    if request.method == 'POST':
        name = request.form['name']
        user = User.users[check]
        user.create_bucketlist(name)
        return render_template("homepage.html",
                               user=user.name,
                               buckets = user.bucketlists)

@app.route('/bucketlist/delete/<id>', methods=['POST'])
def delete_bucket(id=None):
    if request.method == 'POST':
        if id is not None:
            user = User.users[check]
            user.bucketlists.remove(user.bucketlists[int(id)])
        return render_template("homepage.html",
                               user=user.name,
                               buckets = user.bucketlists)

@app.route('/bucketlist/update/<id>', methods=['POST'])
def update_bucket(id=None):
    if request.method == 'POST':
        if id is not None:
            user = User.users[check]
            user.bucketlists[int(id)].finished = True
        return render_template("homepage.html",
                               user=user.name,
                               buckets = user.bucketlists)


@app.route('/')
def homepage():
    if check == -1:
        return redirect(url_for('login'))
    return render_template("homepage.html", buckets=BucketList.bucketlists)

def user_exists(email):
    for existing_user in User.users:
        if existing_user.email.lower() == email.lower():
            return User.users.index(existing_user)

    return -1

if __name__ == '__main__':
    app.run()




