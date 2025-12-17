from flask import Blueprint, render_template
posts_bp = Blueprint('posts', __name__, template_folder='templates')
@posts_bp.route("/posts")
def posts():
    return render_template("Posts/Posts.html")

@posts_bp.route("/create")
def create_post():
    return render_template("Posts/Create.html")
