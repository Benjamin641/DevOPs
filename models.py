from datetime import datetime
from extensions import db


# Model (LIVES HERE)
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)

    userid = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id',
            name='fk_posts_userid_users'
        ),
        nullable=False
    )

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

    user = db.relationship("User", back_populates="posts")

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)

    posts = db.relationship("Post", back_populates="user")

    __table_args__ = (
        db.UniqueConstraint('email', name='uq_users_email'),
    )

    def __init__(self, email, firstname, lastname, phone, password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.password = password