from app.models import Ticket
from app import sqlAlchemy_db
import mysql.connector
from config import Config

def deleteTicket(tick):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT ticketID FROM ticket")
    tickets = mycursor.fetchall()

    ticketInt = int(tick)

    # SQLALCHEMY TEST
    #ticketToRemove = Ticket.query.filter_by(ticketID=int(tick)).first()
    #if ticketToRemove:
    #    sqlAlchemy_db.session.delete(ticketToRemove)
    #    sqlAlchemy_db.session.commit()
    # END TEST
    return True

    for ticket in tickets:
        if ticketInt in ticket:
            sqlStatement = "DELETE FROM ticket WHERE ticketID = %s"
            val = (ticketInt,)  # comma is used to create a tuple with a single element
            mycursor.execute(sqlStatement, val)
            mydb.commit()
            return True
    return False
