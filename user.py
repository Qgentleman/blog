from flask import Blueprint,render_template
user = Blueprint('user',__name__)

@user.route('/haha/')
def fun():
    return render_template('denglu.html')