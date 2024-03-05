from models import User, db


def create_user(email, password, fname, lname):
    """create user in db"""
    user = User(email=email, password=password, fname=fname, lname=lname)
    db.session.add(user)
    db.session.commit()
    return user

def delete_user(email):
    """delete user from db"""
    user = User.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False

def update_user(email, new_fname=None, new_lname=None, new_password=None):
    """update user info in db"""
    user = User.query.filter_by(email=email).first()
    if user:
        if new_fname:
            user.fname = new_fname
        if new_lname:
            user.lname = new_lname
        if new_password:
            user.password = new_password

        db.session.commit()
        return user
    else:
        return None

def verify_user_password(email, password):
    """check that user password matches what's saved"""
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False



def get_user_by_username(username):
    """get user by username"""
    return User.query.filter_by(username=username).first()

def verify_user_password(username, password):
    """check that user password matches what's saved"""
    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False