#coding=gbk
from flask import Flask,render_template,request,url_for,redirect,session
from exts import db
from zd423 import url_list
from laod import url_list2
import re
from models import Navigation,Menu,Article,User,Index
from sqlalchemy import or_
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    # addNav = ([Navigation(navName='��Դ����'),
    #            Navigation(navName='������Ѷ'),
    #            Navigation(navName='����ͼƬ')])
    # db.session.add_all(addNav)
    # db.session.commit()
    # # ������Ŀ�˵�
    # addMenu = ([Menu(mName='ý�岥��', navId=1, link='/media/'),
    #             Menu(mName='�칫���', navId=1, link='/office/'),
    #             Menu(mName='��ҳ���', navId=1, link='/browse/'),
    #             Menu(mName='��Ϸ����', navId=1, link='/game/'),
    #             Menu(mName='�Ƽ���Ѷ', navId=2, link='/technology/'),
    #             Menu(mName='�ȵ���Ѷ', navId=2, link='/hotspot/'),
    #             Menu(mName='����ͼ', navId=3, link='/mmfigure/')])
    # db.session.add_all(addMenu)
    # db.session.commit()
    #������������
    # content_list = url_list2()
    # for inf in content_list:
    #     addArticle = ([Article(aTitle=inf['title'],aTime=inf['time'],aContext=inf['context'],aMid=('5'))])
    #     db.session.add_all(addArticle)
    #     db.session.commit()
    hotsoft = db.session.query(Index.iTitle,Index.iContext).all()
    return render_template('index.html',hotsoft=hotsoft)

#��ҳ����,
#��ַ/part/��Ϊ��ַ��link����
@app.route('/Login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '�ʻ����������������������'
@app.route('/Regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('Base.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.username == username).first()
        if user:
            return'�û����Ѿ�ע�ᣬ������ע��'
        else:
            if password1 != password2:
                return'�������벻��ͬ����˶�'
            else:
                if len(password1) < 6:
                    return '���볤�Ȳ���'
                else:
                    user = User(username=username,password=password1)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('login'))
@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))
@app.route('/Part/<link>')
#��ȡbase.html�е���˵����õ���linkֵ�����뵱ǰ������
def part(link):
    #��ȡҳ��ֵ
    page = request.args.get('page', 1, type=int)
    #��ѯ�˵�����µ��������ݣ�
    pagination = db.session.query(Menu.mId,Menu.mName,Article.aTitle,Article.aTime, Article.aContext).filter( Menu.link == link,Menu.mId == Article.aMid).paginate(
        page, per_page=8, error_out=False)
    content = pagination.items
    # ����ͼ����������vf������չҳ�����
    vf = 'part'

    return render_template('Media.html', content=content, re=re, str=str,vf=vf, pagination=pagination,link=link)
#�������ܺ���
@app.route('/Search/')
def Search():
    link = request.args.get('link')
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter(or_(Article.aTitle.contains(link))).order_by(-Article.aTime).paginate(page, per_page=8, error_out=False)
    content = pagination.items
    # ����ͼ���������Ƹ� vf������չҳ�����
    vf = 'Search'
    return render_template('Search.html',content = content,link=link,vf = vf,re=re,str=str,pagination=pagination)

#������+���Ӻ���
@app.context_processor
def nav_for():
    navName = db.session.query(Navigation.navName,Navigation.navId)
    mName = db.session.query(Menu.mName,Menu.navId,Menu.link)
    return {'navname':navName,'mname':mName}
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user':user}
    return {}
# �Ż�����ע�ͺ���ļ�
# @app.route('/Media/')
# def Media():
#     #��ȡ��Ҫ��ʾ��ҳ��
#     page = request.args.get('page',1, type=int)
#     #per_page ������ÿҳ��ʾ�ļ�¼�ĸ���
#     pagination = db.session.query(Menu.mName,Article.aTitle, Article.aTime, Article.aContext).filter(Article.aMid == 1,Menu.mId == Article.aMid ).paginate(page, per_page=10, error_out=False)
#     posts = pagination.items
#     # content = db.session.query(Menu.mName,Article.aTitle, Article.aTime, Article.aContext).filter(Article.aMid == 1,Menu.mId == 1).all()
#     return render_template('Media.html',content=posts,re=re,str=str,pagination=pagination)
#
# @app.route('/Office/')
# def Office():
#     page = request.args.get('page', 1, type=int)
#     pagination = db.session.query(Menu.mName,Article.aTitle, Article.aTime, Article.aContext).filter(Article.aMid == 2,Menu.mId == Article.aMid).paginate(page, per_page=10, error_out=False)
#     posts = pagination.items
#     return render_template('Office.html',content=posts,re=re,str=str,pagination=pagination)
#
# @app.route('/Browse/')
# def Browse():
#     content = db.session.query(Menu.mName,Article.aTitle, Article.aTime, Article.aContext).filter(Article.aMid == 3,Menu.mId == Article.aMid).all()
#     return render_template('Browse.html',content=content,re=re,str=str)
#
# @app.route('/Phone/')
# def Phone():
#     content = db.session.query(Menu.mName,Article.aTitle, Article.aTime, Article.aContext).filter(Article.aMid == 4,Menu.mId == Article.aMid).all()
#     return render_template('Phone.html',content=content,re=re,str=str)
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
