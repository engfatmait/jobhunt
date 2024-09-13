from jobhunt import db

class jolist(db.Model):
    job_id = db.Column(db.Integer(), primary_key = True)
    jp_id  = db.Column(db.Integer())
    position = db.Column(db.String(length = 30), nullable=False)
    location = db.Column(db.String(length = 50), nullable=False)
    des_req  = db.Column(db.String(length = 1024), nullable=False)

def __init__(self,job_id,jp_id,position, location, des_req):
    self.job_id = job_id
    self.jp_id = jp_id
    self.position = position
    self.location = location
    self.des_req = des_req