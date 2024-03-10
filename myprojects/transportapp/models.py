from transportapp import db


class Item(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    location = db.Column(db.String(length=30),nullable=False,unique=True)
    status = db.Column(db.String(length=10),nullable=False)
    vehicles_count =db.Column(db.Integer(),nullable=False)
    description = db.Column(db.String(length=1024),nullable=False, unique=True)
    def __repr__(self):
        return f"Item(id={self.id}, location='{self.location}', status='{self.status}', vehicles_count={self.vehicles_count}, description='{self.description}')"