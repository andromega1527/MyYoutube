import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from youtube.auth import login_required
from youtube.db import get_db
from youtube.conn import Server
from youtube.load_informs import InformsUser

bp = Blueprint('sla', __name__)
ifms = InformsUser()

def verifyLogin():
    return False if session['user_id'] is '' else True

@bp.route('/index')
def index():
    if verifyLogin() is False:
        return redirect(url_for('auth.login'))

    user = ifms.loadUser(session['user_id'])
    videos = ifms.loadVideos(session['user_id'])
    
    return render_template(
        'index.html',
        user=user,
        videos=videos
    )

@bp.route('/video/<video>')
def video(video):
    if verifyLogin() is False:
        return redirect(url_for('auth.login'))

    user = ifms.loadUser(session['user_id'])
    videos = ifms.loadVideos(session['user_id'])

    for i in videos:
        if i.code == video:
            videoName = i.code + ' - ' + i.title + '.mp4'

    return render_template(
        'video.html',
        user=user,
        videos=videos,
        video=videoName
    )

@bp.route('/new_video', methods=('GET', 'POST'))
def new_video():
    if verifyLogin() is False:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        file = request.form['file']

        Server().sendFile(file)

        redirect(url_for('sla.new_video'))

    return render_template('new_video.html')