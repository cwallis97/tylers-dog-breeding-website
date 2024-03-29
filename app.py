from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import connect_to_db  # Assuming you have a connect_to_db function in models
from crud import create_user, delete_user, update_user, verify_user_password
from send_email import send_email


app = Flask(__name__)

# Assuming connect_to_db initializes the database connection
app.app_context().push()


@app.route('/')
def home():
    tyler_data = {
        'description': 'Some description',
        'image_url': url_for('static', filename='IMG_2445.jpg')  
    }
    return render_template('index.html', tyler_data=tyler_data)

@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        note = request.form.get('message')   

        send_email(email, phone_number)
        return redirect("/thank_you")
    
    return render_template('contact_us.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if verify_user_password(email, password):
            session['user_email'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


@app.route('/create-user', methods=['POST'])
def create_user():
    email = request.form.get('email')
    password = request.form.get('password')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    create_user(email,password,firstname,lastname)
    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(port=5001)