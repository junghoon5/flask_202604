from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def index():
    return 'pybo index!'

@bp.route('/hello')
def hello_world():
    return 'Hello pybo!'

@bp.route('/bye')
def bye_world():
    return 'Bye Pybo!'