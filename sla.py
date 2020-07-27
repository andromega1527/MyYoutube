from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from youtube.auth import login_required
from youtube.db import get_db
from youtube.server import Server
from youtube.session import Session

bp = Blueprint('sla', __name__)
load_session = Session()

ALLOWED_EXTENSIONS = {'mp4'}

def is_allowed_login():
    return session['user_id'] != ''

def is_allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/index')
def index():
    if not is_allowed_login():
        return redirect(url_for('auth.login'))

    user = load_session.get_user_information(session['user_id'])
    videos = load_session.get_video_information(session['user_id'])
    
    return render_template(
        'index.html',
        user=user,
        videos=videos
    )

@bp.route('/video/<video>')
def video(video):
    if not is_allowed_login():
        return redirect(url_for('auth.login'))

    user = load_session.get_user_information(session['user_id'])
    videos = load_session.get_video_information(session['user_id'])

    for i in videos:
        if i.code == video:
            video_name = i.code + i.extension

    return render_template(
        'video.html',
        user=user,
        videos=videos,
        video=video_name
    )

@bp.route('/new_video', methods=('GET', 'POST'))
def new_video():
    if not is_allowed_login():
        return redirect(url_for('auth.login'))

    user = load_session.get_user_information(session['user_id'])
    
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
        if file and is_allowed_files(file.filename):
            filename = secure_filename(file.filename)
            extension = ''

            for i in filename:
                if len(extension) > 0 or i == '.':
                    extension += i

            user.add_video(title, description, extension, file)
            redirect(url_for('sla.index'))

    return render_template(
        'new_video.html',
        user=user
    )