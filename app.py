from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Your database credentials
db_user = "tylereverett"
db_password = "Studmuffin16"
db_name = "MASSWITHCLASS"
db_host = "localhost"
db_port = "5432"

def get_db_connection():
    try:
        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            dbname=db_name,
            host=db_host,
            port=db_port
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error: Unable to connect to the database - {e}")
        return None

def get_db_cursor(connection):
    return connection.cursor()

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

        connection = get_db_connection()
        if connection:
            try:
                with get_db_cursor(connection) as cursor:
                    cursor.execute("INSERT INTO user_inquiries (email, phone_number, note) VALUES (%s, %s, %s)",
                                   (email, phone_number, note))
                    connection.commit()
                    return redirect(url_for('thank_you'))
            except psycopg2.Error as e:
                print(f"Error inserting data into the database - {e}")
            finally:
                connection.close()

    return render_template('contact_us.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True, port=5021)
