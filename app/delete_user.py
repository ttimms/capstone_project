from app.models import User
from app import sqlAlchemy_db
import mysql.connector
from config import Config

def deleteUser(usnm):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT username FROM user")
    nameList = mycursor.fetchall()

    # SQLALCHEMY TEST
    #userToDelete = User.query.filter_by(username=usnm).first()
    #if userToDelete:
    #    sqlAlchemy_db.session.delete(userToDelete)
    #    sqlAlchemy_db.session.commit()
    #    return True
    #return False
    # END TEST

    for name in nameList:
        if usnm in name:
            sqlStatement = "DELETE FROM user WHERE username = %s"
            val = (usnm,)  # comment is used to create a tuple with a single element
            mycursor.execute(sqlStatement, val)
            mydb.commit()
            return True
    return False
