from flask import Blueprint,render_template,request
posts = Blueprint('posts',__name__)

@posts.route('/')
def index():
    return render_template('index.html')
