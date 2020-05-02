from youtube.objects.user import User
from youtube.db import get_db

def loadUser(email):
    db = get_db()
    dbUser = db.execute(
            'SELECT * FROM userMyoutube WHERE email = ?', (email,)
    ).fetchone()
    user = User(dbUser['nameUser'], dbUser['email'], dbUser['passwordUser'], dbUser['permission'])

    return user