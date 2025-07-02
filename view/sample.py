from flask import Flask, render_template,url_for,redirect,session,request,jsonify,flash,make_response,send_file, Blueprint
from datetime import datetime, timedelta
from backend.socketio.socketio import socketio
from dotenv import load_dotenv
import pymysql
import os
import bcrypt

# เรีกก์ใช้งาน Blueprint
sample_Page = Blueprint('sample_Page',__name__)

# โหลดตัวแปรสภาพแวดล้อมจากไฟล์ .env
load_dotenv()

con = pymysql.connect(host=os.environ['ipaddress'],
                             user=os.environ['usernamedb'],
                             password=os.environ['passworddb'],
                             database=os.environ['dbanme'],
                             port=int(os.environ['portdb']),
                             cursorclass=pymysql.cursors.DictCursor,
                             connect_timeout=10,
                             read_timeout=10)
def db_connect():
    global con
    if not con.open:
        con = pymysql.connect(host=os.environ['ipaddress'],
                             user=os.environ['usernamedb'],
                             password=os.environ['passworddb'],
                             database=os.environ['dbanme'],
                             port=int(os.environ['portdb']),
                             cursorclass=pymysql.cursors.DictCursor,
                             connect_timeout=100,
                             read_timeout=100)
    return con

# กำหนดเส้นทางสำหรับ Blueprint
@sample_Page.route('/sample')
def sample_View():
    return render_template('sample/sample.html')
    # return redirect(url_for('home'))

@sample_Page.route('/sample_text', methods=['POST'])
def sample_Ajax():
    data = request.get_json()
    text = data.get('text')
    return jsonify({'text': text + ' from Ajax'})

@socketio.on('test')
def test_Socketio(data):
    text = data.get('text')
    socketio.emit('test', {'test': text + ' from Socketio'})
    # socketio.emit('test', {'test': text + ' from Socketio'}, skip_sid=request.sid)