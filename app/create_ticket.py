from app import sqlAlchemy_db
from app.models import Ticket, Vehicle
from app.email import send_email
from app.sms import send_sms

def createTicket(vtype, desc, loc, amount, lpn):

    message = 'Your vehicle with license plate: ' + lpn + ' has received a ticket.\n' + desc + '\n'

    vehicle = Vehicle.query.filter_by(licensePlateNumber=lpn).first()
    if vehicle:
        owner = vehicle.owner
        if owner:
            if owner.email:
                send_email(owner.email, message)
            if owner.phoneNumber == '3303571702':
                send_sms(owner.phoneNumber, message)

    newTicket = Ticket(
                vType=vtype,
                description=desc,
                location=loc,
                amount=amount,
                licensePlateNumber=lpn)

    sqlAlchemy_db.session.add(newTicket)
    sqlAlchemy_db.session.commit()

    return True
