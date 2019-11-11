from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
# 文章标题title,100, 作者author 20,内容content  最多5000字
db = SQLAlchemy(app)
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(30))
    content = db.Column(db.Text)

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content


# db.create_all()
