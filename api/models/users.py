from..utils import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.Text(), nullable=False)
    is_staff = db.Column(db.Boolean(), default=False)
    is_active = db.Column(db.Boolean(), default=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)
    
