from flask import request,Blueprint,render_template

bp = Blueprint('dash',__name__, url_prefix='/dash')


@bp.route('/')
def index():
    return render_template('dash.html')