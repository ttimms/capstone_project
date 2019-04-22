from app.models import User
from app import sqlAlchemy_db

def deleteUser(usnm):

    userToDelete = User.query.filter_by(username=usnm).first()
    if userToDelete:
        sqlAlchemy_db.session.delete(userToDelete)
        sqlAlchemy_db.session.commit()
        return True
    return False

