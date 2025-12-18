from flask import Blueprint, render_template
import logging

security_bp = Blueprint('security', __name__, template_folder='templates')
logger = logging.getLogger(__name__)
@security_bp.route("/security")
def security():
    logger.info("security page accessed")
    return render_template("Security/security.html")