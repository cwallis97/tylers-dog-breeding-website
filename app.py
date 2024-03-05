from flask import Flask, render_template, request, redirect, url_for
from models import connect_to_db  # Assuming you have a connect_to_db function in models
from crud import create_user, delete_user, update_user, verify_user_password

app = Flask(__name__)

# Assuming connect_to_db initializes the database connection
connect_to_db(app)


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
        return redirect("/thank_you")
    
    return render_template('contact_us.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    # Create a new user
    new_user = create_user(email="example@example.com", password="password123", fname="John", lname="Doe")
    print(f"User created: {new_user}")

    # Delete a user by email
    deleted = delete_user(email="example@example.com")
    if deleted:
        print("User deleted successfully")
    else:
        print("User not found or deletion failed")

    # Update user information
    updated_user = update_user(email="example@example.com", new_fname="UpdatedJohn", new_lname="UpdatedDoe", new_password="newpassword123")
    if updated_user:
        print(f"User updated: {updated_user}")
    else:
        print("User not found")

    # Verify user password
    email_to_verify = "example@example.com"
    password_to_verify = "newpassword123"
    if verify_user_password(email=email_to_verify, password=password_to_verify):
        print("Password verified successfully")
    else:
        print("Incorrect password or user not found")
