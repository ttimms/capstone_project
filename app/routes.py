#import os
from app import app, sqlAlchemy_db
from flask import request, render_template, redirect, url_for
from app.email import send_email
from app.sms import send_sms
#from app.login_verification import loginVerification
from app.create_user import createUser
from app.delete_user import deleteUser
from app.display_users import displayUsers
from app.create_ticket import createTicket
from app.delete_ticket import deleteTicket
from app.view_tickets import viewTickets
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Ticket, Vehicle
from werkzeug.security import check_password_hash, generate_password_hash
from app.visionApiTest import cloudAPI
#from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.role == "Associate":
        return render_template('create_delete_ticket.html')
    if current_user.role == "Admin" or current_user.role == "Manager":
        return redirect(url_for('view_tickets'))
    return render_template('edit_profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or check_password_hash(user.password, request.form['password']) == False:
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/send_mail', methods=['GET', 'POST'])
@login_required
def send_email_alert():
    if current_user.role == "Customer":
        return redirect(url_for('index'))
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
@login_required
def send_sms_alert():
    if current_user.role == "Customer":
        return redirect(url_for('index'))
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
@login_required
def create_database_user():
    if current_user.role == "Customer" or current_user.role == "Associate":
        return redirect(url_for('index'))
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
@login_required
def create_ticket():
    if current_user.role == "Customer":
        return redirect(url_for('index'))
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
@login_required
def delete_database_user():
    if current_user.role == "Customer" or current_user.role != "Associate":
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        if deleteUser(username) == True:
            return 'Success. Check that the user record was properly deleted.'
        return 'Error. Cannot find provided user in database'
    return 'Failure. Invalid request type'

@app.route('/delete_ticket', methods=['GET', 'POST'])
@login_required
def delete_ticket():
    if current_user.role == "Customer":
        return redirect(url_for('index'))
    if request.method == 'POST':
        ticket_Id = request.form['tick_id']
        if deleteTicket(ticket_Id) == True:
            return 'Success. Check that the ticket was properly deleted.'
        return 'Error. Cannot find provided ticketID in database'
    return 'Failure. Invalid request type'

@app.route('/display_users', methods=['GET', 'POST'])
@login_required
def display_users():
    if current_user.role == "Customer" or current_user.role == "Associate":
        return redirect(url_for('index'))
    nameList = displayUsers()
    return render_template('display_users.html', nameList=nameList)

@app.route('/view_tickets', methods=['GET', 'POST'])
@login_required
def view_tickets():
    if request.method == 'POST':
        lpn = request.form['licenseplate']
        ticketRecords = viewTickets(lpn)
        return render_template('view_tickets.html', ticketRecords=ticketRecords)

    if request.method == 'GET':
        ticketRecords = Ticket.query.all()
        return render_template('view_tickets.html', ticketRecords=ticketRecords)

@app.route('/modify_user_data', methods=['GET'])
@login_required
def modify_user_data():
    if current_user.role == "Customer" or current_user.role == "Associate":
        return redirect(url_for('index'))
    return render_template('modify_user_data.html')

@app.route('/create_delete_ticket', methods=['GET'])
@login_required
def create_delete_ticket():
    if current_user.role == "Customer":
        return redirect(url_for('index'))
    lpn = ''
    return render_template('create_delete_ticket.html', lpn=lpn)


#-----------------------------Here
@app.route('/create_delete_ticket', methods=['POST'])
def upload_file():
    #file = request.files['image']
    #f = os.path.join(app.config['/home/copilot/visionAPI'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    #file.save(f)

    #return render_template('index.html')
    file = request.form['file']
    lpn = cloudAPI(file).first()
    return render_template('create_delete_ticket.html', lpn=lpn)

#---------------------------------------------------------

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        pass1 = request.form['password']
        pass2 = request.form['password2']
        if pass1 == pass2:
            current_user.username = request.form['username']
            current_user.email = request.form['email']
            current_user.password = generate_password_hash(request.form['password'])
            current_user.firstName = request.form['firstName']
            current_user.lastName = request.form['lastName']
            current_user.phoneNumber = request.form['phone']
            sqlAlchemy_db.session.commit()

    return render_template('edit_profile.html')

@app.route('/add_vehicle', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    if request.method == 'POST':
        newVehicle = Vehicle(
                        licensePlateNumber=request.form['lpn'],
                        make=request.form['make'],
                        model=request.form['model'],
                        id=current_user.id)
        sqlAlchemy_db.session.add(newVehicle)
        sqlAlchemy_db.session.commit()
    return render_template('add_vehicle.html')

@app.route('/send_notification', methods=['GET', 'POST'])
@login_required
def send_notification():
    if request.method == 'GET':
        return render_template('send_notification.html')
    vehicle = Vehicle.query.filter_by(licensePlateNumber=request.form['licensePlate']).first()
    if vehicle:
        owner = vehicle.owner
        if owner:
            if owner.email:
                send_email(owner.email, request.form['message'])
            if owner.phoneNumber:
                send_sms(owner.phoneNumber, request.form['message'])
    return redirect(url_for('index'))
