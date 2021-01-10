from werkzeug.security import generate_password_hash, check_password_hash
from app import db, app, login_manager


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True, primary_key=True)
    password_hash = db.Column(db.String(128))
    events = db.relationship('Event', backref='author', lazy='dynamic', primaryjoin="User.email == Event.author_email")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    author_email = db.Column(db.String(120), db.ForeignKey('user.email'))
