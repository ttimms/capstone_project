from app.models import User
from werkzeug.security import check_password_hash
import mysql.connector
from config import Config

def loginVerification(usnm, pswd):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT username, password FROM user")

    nameList = mycursor.fetchall()

    # SQLALCHEMY TEST
    #users = User.query.all()
    #for u in users:
    #    if u.username == usnm and check_password_hash(u.password, pswd) == True:
    #        return True
    #return False
    # END TEST

    if (usnm, pswd) in nameList:
        return True
    return False
