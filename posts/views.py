from flask import Blueprint, render_template
import logging
posts_bp = Blueprint('posts', __name__, template_folder='templates')
logger = logging.getLogger(__name__)
@posts_bp.route("/posts")
def posts():
    logger.info("posts page accessed")
    return render_template("Posts/Posts.html")

@posts_bp.route("/create")
def create_post():
    logger.info("createpost page accessed")
    return render_template("Posts/Create.html")
