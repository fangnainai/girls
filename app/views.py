# -*- coding:utf-8 -*-
from app import app
from flask import render_template
from flask import session
from flask import flash
from flask import request
from flask import json
from flask import jsonify
from home import dataProduct
@app.route('/')
def index():
    user = {'nickname': 'ff'}
    return render_template("index.html",title = 'Home', user = user)
@app.route('/login',methods=['GET','POST'])
def login():
    if session['login'] == True:
        print '已登陆'
    return render_template("login.html")
@app.route('/loginVerify',methods=['GET','POST'])
def loginVerify():
    info = json.loads(request.data)
    user_name = info['user_name']
    user_password = info['user_password']
    print user_name,user_password
    data = dataProduct()
    result = data.loginVerify(user_name)
    if result == user_password:
        print "true"
        flash(u'登录成功!')
        session['login'] = True
        session['userid'] = user_name
        print session
        return jsonify({'ok': 'True'})

    else:
        print "false"
        return jsonify({'ok': 'False'})

@app.route('/drawBar/<content>')
def drawBar(content):
    data = dataProduct()
    result = data.drawBar(content)
    #print result
    x = []
    y = []
    xs = []
    for i in result:
        x.append(i[0])
        y.append(i[1])
    xs.append(x)
    xs.append(y)
    print xs
    return render_template("draw_bar.html",xs=xs)

@app.route('/drawLoad',methods=['GET','POST'])
def drawLoad_index():
    return render_template("draw_load.html")
@app.route('/draw_Load',methods=['GET','POST'])
def drawLoad():
    content = json.loads(request.data)
    data = dataProduct()
    result = data.drawBar(content)
    # print result
    x = []
    y = []
    xs = []
    for i in result:
        x.append(i[0])
        y.append(i[1])
    xs.append(x)
    xs.append(y)
    print xs
    return jsonify({'ok': xs})














