from app.models import Ticket
import mysql.connector
from config import Config

def viewTickets(lpn):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    sqlStatement = "SELECT * FROM ticket WHERE licensePlateNumber = %s"

    val = (lpn,)

    mycursor.execute(sqlStatement, val)
    tickets = mycursor.fetchall()

    return tickets

    # SQLACLHEMY TEST
    #ticketList = Ticket.query.filter_by(licensePlateNumber=lpn)
    #return ticketList
    # END TEST