from flask import Blueprint, redirect, url_for

from pybo.models import Question

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

