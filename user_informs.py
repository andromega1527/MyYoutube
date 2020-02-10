from youtube.objects.user import Usuario
from youtube.db import get_db

def loadUser(email):
    db = get_db()
    dbUser = db.execute(
            'SELECT * FROM userMyoutube WHERE email = ?', (email,)
    ).fetchone()
    user = Usuario(dbUser['nameUser'], dbUser['email'], dbUser['passwordUser'], dbUser['permission'])

    return user