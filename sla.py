import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from youtube.auth import login_required
from youtube.db import get_db

bp = Blueprint('sla', __name__)

@bp.route('/index')
def index():
    return render_template('index.html')