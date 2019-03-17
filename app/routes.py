from app import app
from flask import request, render_template
from app.email import send_email
from app.sms import send_sms
from app.login_verification import loginVerification
from app.create_user import createUser
from app.delete_user import deleteUser
from app.display_users import displayUsers
from app.create_ticket import createTicket
from app.delete_ticket import deleteTicket
from app.view_tickets import viewTickets

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['username']
        pass_ = request.form['password']
        if loginVerification(user, pass_) == True:
            return render_template('api_test.html')
    return render_template('login.html')

@app.route('/send_mail', methods=['GET', 'POST'])
def send_email_alert():
    if request.method == 'POST':
        Password = request.form['Password']
        if Password == 'password':
            Email = request.form['Email']
            Message = request.form['Message']
            send_email(Email, Message)
            return 'Success. Check that email was properly delivered.'
        return 'Invalid password'
    return 'Failure. Invalid request type'

@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms_alert():
    if request.method == 'POST':
        Password = request.form['Password']
        if Password == 'password':
            Phone = request.form['Phone']
            Message = request.form['Message']
            send_sms(Phone, Message)
            return 'Success. Check that the message was properly delivered.'
        return 'Invalid password'
    return 'Failure. Invalid request type'

@app.route('/create_user', methods=['GET', 'POST'])
def create_database_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pass_ = request.form['password']
        fn = request.form['firstName']
        ln = request.form['lastName']
        phone = request.form['phone']
        role = request.form['role']
        if createUser(username, email, pass_, fn, ln, role, phone) == True:
            return 'Success. Check that the entry was properly inserted.'
        return 'Error. Check the python function from create_user.py'
    return 'Failure. Invalid request type'

@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        vtype = request.form['vtype']
        desc = request.form['description']
        loc = request.form['location']
        amount = request.form['amount']
        lpNum = request.form['lpn']
        if createTicket(vtype, desc, loc, amount, lpNum) == True:
            return 'Success. Check that the ticket was successfully entered in database.'
        return 'Error. Check the python function from create_ticket.py'
    return 'Failure. Invalid request type'

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_database_user():
    if request.method == 'POST':
        username = request.form['username']
        if deleteUser(username) == True:
            return 'Success. Check that the user record was properly deleted.'
        return 'Error. Cannot find provided user in database'
    return 'Failure. Invalid request type'

@app.route('/delete_ticket', methods=['GET', 'POST'])
def delete_ticket():
    if request.method == 'POST':
        ticket_Id = request.form['tick_id']
        if deleteTicket(ticket_Id) == True:
            return 'Success. Check that the ticket was properly deleted.'
        return 'Error. Cannot find provided ticketID in database'
    return 'Failure. Invalid request type'

@app.route('/display_users', methods=['GET', 'POST'])
def display_users():
    nameList = displayUsers()
    return render_template('display_users.html', nameList=nameList)

@app.route('/view_tickets', methods=['GET', 'POST'])
def view_tickets():
    if request.method == 'POST':
        lpn = request.form['licenseplate']
        ticketRecords = viewTickets(lpn)
        return render_template('view_tickets.html', ticketRecords=ticketRecords)