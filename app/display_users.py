from app.models import User
import mysql.connector
from config import Config

def displayUsers():
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

    returnList = []
    index = 0
    for name in nameList:
        returnList.insert(index, name[0])
        index += 1
    return returnList



    # SQLALCHEMY TEST
    #userList = User.query.all()
    #return userList
    # END TEST