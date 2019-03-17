from app import sqlAlchemy_db
from app.models import Ticket
import mysql.connector
from config import Config

def createTicket(vtype, desc, loc, amount, lpn):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    sqlStatement = "INSERT INTO ticket(type, description, location, amount, licensePlateNumber) VALUES(%s, %s, %s, %s, %s)"
    vals = (vtype, desc, loc, amount, lpn)

    mycursor.execute(sqlStatement, vals)

    mydb.commit()
    mycursor.execute("SELECT type, description, location, amount, licensePlateNumber FROM ticket")

    # SQL ALCHEMY TEST

    newTicket = Ticket(
                vType=vtype,
                description=desc,
                location=loc,
                amount=amount,
                licensePlateNumber=lpn)

    sqlAlchemy_db.session.add(newTicket)
    sqlAlchemy_db.session.commit()

    # END TEST

#    nameList = mycursor.fetchall()

#    if (vtype, desc, loc, amount, lpn) in nameList:
#        return True
    return True
