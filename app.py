from flask import Flask, render_template
import logging_config
import logging


from extensions import db , migrate

from accounts.views import accounts_bp
from posts.views import posts_bp
from security.views import security_bp

app = Flask(__name__)
app.config.from_object("config")
logging.info("Flask application starting")

db.init_app(app)
migrate.init_app(app, db)


# Blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(security_bp)
@app.errorhandler(500)
def internal_error(error):
    logging.exception("Internal server error occurred")
    return "Internal Server Error", 500

@app.route("/")
def index():
    return render_template("Home/index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)