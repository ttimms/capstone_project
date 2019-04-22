from app import sqlAlchemy_db
from app.models import User
from werkzeug.security import generate_password_hash

def createUser(usnm, email, pswd, fn, ln, role, phoneNum):

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

    return True
