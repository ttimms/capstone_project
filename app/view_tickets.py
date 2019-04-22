from app.models import Ticket

def viewTickets(lpn):

    ticketList = Ticket.query.filter_by(licensePlateNumber=lpn)
    return ticketList