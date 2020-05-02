from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from youtube.auth import login_required
from youtube.db import get_db
from youtube.conn import Server
from youtube.video_informs import loadVideos
from youtube.user_informs import loadUser

bp = Blueprint('sla', __name__)

ALLOWED_EXTENSIONS = {'mp4'}

def verifyLogin():
    return False if session['user_id'] is '' else True

def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/index')
def index():
    if verifyLogin() is False:
        return redirect(url_for('auth.login'))

    user = loadUser(session['user_id'])
    videos = loadVideos(session['user_id'])
    
    return render_template(
        'index.html',
        user=user,
        videos=videos
    )

@bp.route('/video/<video>')
def video(video):
    if verifyLogin() is False:
        return redirect(url_for('auth.login'))

    user = loadUser(session['user_id'])
    videos = loadVideos(session['user_id'])

    for i in videos:
        if i.code == video:
            videoName = i.code + i.extension

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
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        title = request.form['title']
        description = request.form['description']
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            user = loadUser(session['user_id'])
            extension = ''

            for i in filename:
                if len(extension) > 0 or i == '.':
                    extension += i

            user.add_video(title, description, extension, file)
            # return redirect(url_for('uploaded_file', 
            #         filename=filename
            # ))
            redirect(url_for('sla.index'))

    return render_template('new_video.html')