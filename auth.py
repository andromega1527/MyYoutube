import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from youtube.db import get_db
# import HTTPServer as server
# import SocketServer

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Precisa do nome de usuário.'
        elif not password:
            error = 'Precisa da senha.'
        elif db.execute(
            'SELECT email FROM user WHERE nome = ?', (username)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash(error)

    return render_template('register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE nome = ?', (username)
        ).fetchone()

        if user is None:
            error = 'Nome incorreto :('
        elif not check_password_hash(user['password'], password):
            error = 'Senha incorreta :('

        if error is None:
            session.clear()
            session['user_id'] = user['email']
            return redirect(url_for('index'))
    
        flash(error)

    return render_template('login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

# def run():
#     port = 8080
#     handler = server.SimpleHTTPRequestHandler
#     httpd = SocketServer.TCPServer(('', port), handler)
#     httpd.serve_forever()

# if __name__ == '__main__':
#     app.run(debug=True)