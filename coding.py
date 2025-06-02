from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Needed for flash messages

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'akshaypt10@gmail.com'
app.config['MAIL_PASSWORD'] = '----------------------'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_mail', methods=['POST'])
def send_message():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if not all([name, email, subject, message]):
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))
        
        msg = Message(
            subject=f"Portfolio Contact: {subject}",
            sender=email,
            recipients=['akshaypt10@gmail.com']
        )
        msg.body = f"""
        From: {name}
        Email: {email}
        
        Message:
        {message}
        """
        
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('index'))
    
    except Exception as e:
        app.logger.error(f"Error sending email: {str(e)}")
        flash('An error occurred while sending your message. Please try again later.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
