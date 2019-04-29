from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import func
from . import login_manager

class User(db.Model,UserMixin):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255),unique=True)
	email=db.Column(db.String(255),unique=True)
	password=db.Column(db.String(255))
	writer=db.Column(db.Boolean, default=False)
	created_at = db.Column(db.DateTime, index=True, default=func.now())
	updated_at = db.Column(db.DateTime, default=func.now())
	posts = db.relationship('Post', backref='user', lazy='dynamic')
	comments = db.relationship('Comment', backref='user', lazy='dynamic')

	def verifypass(self,pass_check):
		return check_password_hash(self.password,pass_check)

	@property
	def passwd(self):
		raise AttributeError('You cannot read this!')

	@passwd.setter
	def passwd(self,passwd):
		self.password = generate_password_hash(passwd)

	def save(self):
		db.session.add(self)
		db.session.commit()
		
	def __repr__(self):
		return '<User %r>' % self.username

class Post(db.Model):
	__tablename__='posts'
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(255))
	text=db.Column(db.Text())
	user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
	category=db.Column(db.String(255))
	created_at = db.Column(db.DateTime, index=True, default=func.now())
	updated_at = db.Column(db.DateTime, default=func.now())
	comments=db.relationship('Comment', backref='post', lazy='dynamic')

	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete_(self):
		for items in self.likes.all()+self.dislikes.all()+self.comments.all():
			items.delete_()
		db.session.delete(self)
		db.session.commit()

class Comment(db.Model):
	__tablename__='comments'
	id=db.Column(db.Integer,primary_key=True)
	user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
	post_id=db.Column(db.Integer, db.ForeignKey('posts.id'))
	text=db.Column(db.Text())
	created_at = db.Column(db.DateTime, index=True, default=func.now())
	updated_at = db.Column(db.DateTime, default=func.now())
	def save(self):
		db.session.add(self)
		db.session.commit()
	def delete_(self):
		db.session.delete(self)
		db.session.commit()

@login_manager.user_loader
def usergetter(uid):
	return User.query.get(uid)
