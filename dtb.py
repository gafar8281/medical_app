from flask import Flask, render_template, request ,session
from dtb2 import users_collection
from flask_session import Session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gafar_abdul'

# Session configuration
app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_USE_SIGNER'] = False

# Initialize the Flask-Session extension
Session(app)


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        #Retrieve login credentials from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Check the credentials against the stored user data in MongoDB
        user=users_collection.find_one({'username': username, 'password': password})
        if user:
            session['company-name'] = user['full_name']
            session['user-name'] = user['username']
            session['address-value'] = user['address']
            session['email-value'] = user['email']
            session['phone-value'] = user['phone_number']
            return render_template('homepage.html')
        else:
            # Invalid credentials, you may want to show an error message
            return render_template('index.html', error='Invalid username or password')
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # Retrieve user input from the registration form
        full_name = request.form.get('full_name')
        username = request.form.get('username')
        address = request.form.get('address')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        confirm_password = request.form.get('Confirm_Password')

        # Insert user data into the MongoDB collection
        user_data = {
            'full_name': full_name,
            'username': username,
            'address': address,
            'email': email,
            'phone_number': phone_number,
            'password': password,
            'Confirm_Password':confirm_password
        }
        users_collection.insert_one(user_data)

        # Redirect to the home page or any other page after successful registration
        return render_template('index.html')

    return render_template('signup.html')

@app.route('/allitems')
def allitems():
    return render_template('allitems.html')

@app.route('/additems')
def additems():
    return render_template('additems.html')

@app.route('/submit', methods=['POST'])
def submit():
    # if request.method == 'POST':
        # Redirect to the homepage
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
