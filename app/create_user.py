from app import sqlAlchemy_db
from app.models import User
from werkzeug.security import generate_password_hash
import mysql.connector
from config import Config

def createUser(usnm, email, pswd, fn, ln, role, phoneNum):
    #setup object for db connection
    mydb = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USERNAME,
        passwd=Config.DB_PASSWORD,
        database=Config.DB_CURRENT
        )

    mycursor = mydb.cursor()

    sqlStatement = "INSERT INTO user(email, password, username, firstName, lastName, role, phoneNumber) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    vals = (email, pswd, usnm, fn, ln, role, phoneNum)

    mycursor.execute(sqlStatement, vals)

    mydb.commit()

    # SQL ALCHEMY TEST

    newUser = User(
                username=usnm,
                email=email,
                password=generate_password_hash(pswd),
                firstName=fn,
                lastName=ln,
                role=role,
                phoneNumber=phoneNum)

    sqlAlchemy_db.session.add(newUser)
    sqlAlchemy_db.session.commit()

    # END TEST

    mycursor.execute("SELECT username, password, email, firstName, lastName, role, phoneNumber FROM user")
    nameList = mycursor.fetchall()

    if (usnm, pswd, email, fn, ln, role, phoneNum) in nameList:
        return True
    return False
