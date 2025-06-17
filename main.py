from flask import Flask, render_template,url_for,redirect,session,request,jsonify,flash,make_response,send_file, Blueprint
from datetime import datetime, timedelta
from backend.socketio.socketio import socketio
from dotenv import load_dotenv
import pymysql
import os
import bcrypt

# เรีกก์ใช้งาน Blueprint
from view.sample import sample_Page

load_dotenv()
con = pymysql.connect(host=os.environ['ipaddress'],
                             user=os.environ['usernamedb'],
                             password=os.environ['passworddb'],
                             database=os.environ['dbanme'],
                             port=int(os.environ['portdb']),
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
                             connect_timeout=100,
                             read_timeout=100)
    return con

app = Flask(__name__)

app.secret_key='secret_key_for_you' # ควรเปลี่ยนเป็นคีย์ที่ปลอดภัยและไม่เปิดเผย
app.permanent_session_lifetime = timedelta(days=1) # กำหนดอายุของ session ตามต้องการ

# เพิ่มเติม Blueprint
app.register_blueprint(sample_Page)

socketio.init_app(app)

# กำหนดเส้นทางหลัก
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)