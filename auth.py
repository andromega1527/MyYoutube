import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from youtube.db import get_db
from youtube.server import Server

bp = Blueprint('auth', __name__, url_prefix='/auth')

def verifyLogin():
    return False if len(session) > 0 else True

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
    if verifyLogin() is False:
        return redirect(url_for('sla.index'))
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (username,)
        ).fetchone()

        if user is None or check_password_hash(user['senha'], password) == 'False' or user['senha'] != password:
            error = 'Nome de usuário ou senha incorretos.'

        if error is None:
            session.clear()
            session['user_id'] = user['email']
            Server().connect(session['user_id'])
            return redirect(url_for('sla.index')) #(arquivo python).(função que renderiza a pagina)
    
        flash(error)
    
    return render_template('login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM userMyoutube WHERE email = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    Server().close_connection()
    return redirect(url_for('auth.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view