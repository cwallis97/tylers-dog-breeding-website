from flask import Flask, render_template, request, redirect, url_for
import models, crud

app = Flask(__name__)
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

    return render_template('contact_us.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    models.connect_to_db(app)
    app.run(debug=True)