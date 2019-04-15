from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods = ['POST'])
def errors():

#verify username
    username = request.form['username']
    username_error = ''

    if username == '':
        username_error = "Please enter a valid Username."

    elif len(username) < 3 or len(username) > 20:
        username_error = "Please enter a valid Username between 3 and 20 characters."
        username = ''
    elif ' ' in username:
        username_error = "Please omit spaces from your Username."
        username = ''
    
#Verify password
    password = request.form['password']
    password_error = ''
    
    if password == '':
        password_error = "Please enter a Password."
    
    elif len(password) < 3 or len(username) > 20:
        password_error = "Please enter a valid Username between 3 and 20 characters."

    elif ' ' in password:
        password_error = "Please omit spaces from your Password."

#Verify verified password

    verify = request.form['verify']
    verify_error = ''

    if verify == '':
        verify_error = "Please re-enter your password."

    elif verify != password:
        verify_error = "Passwords do not match.  Please re-enter your password."

#verify email

    email = request.form['email']
    email_error = ''

    if len(email) < 1:
        email = ''
    elif (email.count(".")!=1) or (email.count("@")!=1) or (" " in email):
        email_error = "Please enter a valid email."
        email = ''

#return
    if not email_error and not verify_error and not password_error and not username_error:
        return redirect('/Welcome?username={0}'.format(username))
    else:
        return render_template('index.html', 
            username_error=username_error,
            username=username,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error,
            email=email)




@app.route("/Welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()
