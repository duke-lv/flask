import functools
from flask import(
    Blueprint, flash, g, redirect,  render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from src.db import get_db
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required!'
        elif not pwd:
            error = 'Password is required!'