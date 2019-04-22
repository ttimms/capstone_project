from app.models import User

def displayUsers():

    userList = User.query.all()
    return userList