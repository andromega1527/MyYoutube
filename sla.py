import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from youtube.auth import login_required
from youtube.db import get_db
import os

bp = Blueprint('sla', __name__)

def cleanNamesImages(name):
    newName = ''

    for i in name:
        if i != '.':
            newName += i
        else:
            break
    
    return newName

@bp.route('/index')
def index():
    videos = os.listdir('//home/leonam/Projetos/myoutube/youtube/videos/')
    cleanVideosNames = [cleanNamesImages(i) for i in videos]
    return render_template('index.html', cleanVideosNames=cleanVideosNames, videos=videos)

@bp.route('/video')
def video():
    return render_template('video.html')