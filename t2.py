from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

app = Flask(__name__)

from urllib.parse import quote_plus

# Your MongoDB connection string
username = "abdulgafar8281"
password = "Gafar@123"

# Escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)


# Connect to MongoDB
client = MongoClient(f"mongodb+srv://{escaped_username}:{escaped_password}@cluster85.yxziyhj.mongodb.net/?retryWrites=true&w=majority")
db = client['Medical']
users_collection = db['demo2']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        password = request.form.get('Password')
        confirm_password = request.form.get('Confirm_Password')

        # Check if the username already exists
        if users_collection.find_one({'username': username}):
            return render_template('signup.html', message='Username already exists. Try a different one.')

        # Check if the email already exists
        if users_collection.find_one({'email': email}):
            return render_template('signup.html', message='Email already exists. Try a different one.')

        # Check if passwords match
        if password != confirm_password:
            return render_template('signup.html', message='Passwords do not match.')

        # Hash the password before storing it
        # password = "user_input_password"
        if password is None:
            return render_template('signup.html', message='Password cannot be empty.')

        hashed_password = generate_password_hash(password, method='sha256')


        # Insert the user into the database
        users_collection.insert_one({
            'full_name': full_name,
            'username': username,
            'email': email,
            'phone_number': phone_number,
            'password': hashed_password
        })

        # Redirect to the home page or another page after successful registration
        # return redirect(url_for('/index'))

        return render_template('about.html')
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)




