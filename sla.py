import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from youtube.auth import login_required
from youtube.db import get_db
import os
from youtube.objects.usuario import Usuario
from youtube.objects.video import Video
from youtube.db import get_db

bp = Blueprint('sla', __name__)

def logoff():
    session['user_id'] = '' 

def verifyLogin():
    if session['user_id'] in (None, ''):
        return redirect(url_for('auth.login'))

def loadUser(email):
    db = get_db()
    dbUser = db.execute(
            'SELECT * FROM userMyoutube WHERE email = ?', (email,)
    ).fetchone()
    user = Usuario(dbUser['nameUser'], dbUser['email'], dbUser['passwordUser'], dbUser['permission'], dbUser['video'], dbUser['playlist'])

    return user

def loadVideos(email):
    db = get_db()
    videos = []
    dbVideo = db.execute(
        'SELECT video.code, video.nameVideo, video.descriptionVideo, video.localization \
        FROM video_details \
        INNER JOIN userMyoutube ON video_details.code_user = userMyoutube.email \
        INNER JOIN video ON video_details.code_video = video.code \
        WHERE userMyoutube.email = ?', (email,)
    ).fetchall()

    for i in dbVideo:
        video_informs = []
        for j in i:
            video_informs.append(j)
        
        video = Video(video_informs[0], video_informs[1], video_informs[2], video_informs[3])
        videos.append(video)

    return videos

@bp.route('/index')
def index():
    verifyLogin()
    user = loadUser(session['user_id'])
    videos = loadVideos(session['user_id'])
    videosName = []
    for i in videos:
        videosName.append(i.title)

    return render_template(
        'index.html',
        user=user,
        videosName=videosName
    )

@bp.route('/video')
def video():
    verifyLogin()
    return render_template('video.html')