from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:111111@localhost/pythonclass'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# 文章标题title,100, 作者author 20,内容content  最多5000字
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

# html
# 视图函数  --  接口
# 数据库


# 主机/index            --> 所有的文章
#
#               点击标题跳转到博客详情页
#
# 主机/blog/博客id  --> 查看某篇文章
#         -------404 界面
# 主机/newblog/      --> 新建文章
#
# 主机/editblog/<博客编号id>
#                                 --> 修改文章
#
# 主机/delblog/<博客编号id>
#                                  --> 删除文章

# @app.route('/index')
# def index():
#     # todo
#     # blogs = query
#
#     return render_template('index.html', blogs=blogs)


@app.route('/')
def index1():
    #  从数据库查询到所有数据
    blogs = Blog.query.all()
    # print(type(blogs))
    # for blog in blogs:
    #     print(blog.title)
    return render_template('index.html', blogs=blogs)


@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).one()
    return render_template('show_blog.html', blog=blog)


@app.route('/editblog/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id).one()
    if request.method == 'GET':
        return render_template('edit_blog.html', blog=blog)
    else:
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        blog.title = title
        blog.author = author
        blog.content = content
        db.session.commit()
        return redirect(url_for('show_blog', blog_id=blog.id))


@app.route('/delblog/<int:blog_id>')
def del_blog(blog_id):
    # 从数据库中查询到相应数据,删除
    blog = Blog.query.filter_by(id=blog_id).one()
    db.session.delete(blog)
    db.session.commit()
    return redirect('/')
    # return render_template('del_blog.html')


@app.route('/newblog', methods=['GET', 'POST'])
def new_blog():
    # todo
    # blog1 = Blog(title='firstblog',author='xxx@qq.com',content='测试数据')
    # db.session.add(blog1)
    # db.session.commit()
    # get ==>返回表单
    # post ==> 向数据库里添加数据
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        # 获取数据
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        blog1 = Blog(title=title, author=author, content=content)
        db.session.add(blog1)
        db.session.commit()
        return '添加成功'


@app.errorhandler(404)
def not_find(e):
    return '没找到界面'


if __name__ == '__main__':
    app.run()

# 其他
# 蓝图
# 分页
# wtf
# 界面美化
# 登录   表  界面
# 代码分离
# 配置文件 隔离开, 千万别提交到git
