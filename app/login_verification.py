from app.models import User
from werkzeug.security import check_password_hash

def loginVerification(usnm, pswd):

    users = User.query.all()
    for u in users:
        if u.username == usnm and check_password_hash(u.password, pswd) == True:
            return True
    return False
