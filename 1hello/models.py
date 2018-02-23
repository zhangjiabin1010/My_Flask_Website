from exts import db
class Navigation(db.Model):
    __tablename__ ='navigation'
    navId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    navName = db.Column(db.String(20))
# 创建菜单表
class Menu(db.Model):
    __tablename__ = 'menu'
    mId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    mName = db.Column(db.String(20))
    link = db.Column(db.String(50))
    navId = db.Column(db.Integer,db.ForeignKey('navigation.navId'))
class Article(db.Model):
    __tablename__ = 'article'
    aId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    aTitle = db.Column(db.String(50))
    aTime = db.Column(db.String(20))
    aContext = db.Column(db.Text)
    aMid = db.Column(db.Integer,db.ForeignKey('menu.mId'))
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
class Index(db.Model):
    __tablename__ = 'index'
    iId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    iTitle = db.Column(db.String(50))
    iContext = db.Column(db.Text)
    idd = db.Column(db.Integer)
