from app.models import Ticket
from app import sqlAlchemy_db

def deleteTicket(tick):

    ticketToRemove = Ticket.query.filter_by(ticketID=int(tick)).first()
    if ticketToRemove:
        sqlAlchemy_db.session.delete(ticketToRemove)
        sqlAlchemy_db.session.commit()
        return True
    return False