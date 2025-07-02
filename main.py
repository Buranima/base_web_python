from flask import Flask, render_template,url_for,redirect,session,request,jsonify,flash,make_response,send_file, Blueprint
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime, timedelta
from backend.socketio.socketio import socketio
from dotenv import load_dotenv
import pymysql
import os
import bcrypt

# เรีกก์ใช้งาน Blueprint
from view.sample import sample_Page

# โหลดตัวแปรสภาพแวดล้อมจากไฟล์ .env
load_dotenv()

# กำหนดการเชื่อมต่อฐานข้อมูล
# con = pymysql.connect(host=os.environ['ipaddress'],
#                              user=os.environ['usernamedb'],
#                              password=os.environ['passworddb'],
#                              database=os.environ['dbanme'],
#                              port=int(os.environ['portdb']),
#                              cursorclass=pymysql.cursors.DictCursor,
#                              connect_timeout=10,
#                              read_timeout=10)
# def db_connect():
#     global con
#     if not con.open:
#         con = pymysql.connect(host=os.environ['ipaddress'],
#                              user=os.environ['usernamedb'],
#                              password=os.environ['passworddb'],
#                              database=os.environ['dbanme'],
#                              port=int(os.environ['portdb']),
#                              cursorclass=pymysql.cursors.DictCursor,
#                              connect_timeout=100,
#                              read_timeout=100)
#     return con

app = Flask(__name__)

app.secret_key='secret_key_for_you' # ควรเปลี่ยนเป็นคีย์ที่ปลอดภัยและไม่เปิดเผย
app.config['UPLOAD_FOLDER'] = 'path_upload' # กำหนดโฟลเดอร์สำหรับอัพโหลดไฟล์
app.config['PREFERRED_URL_SCHEME'] = 'https' # กำหนด URL scheme เป็น https
app.config['SESSION_COOKIE_SECURE'] = True # ใช้กับ HTTPS เท่านั้น
app.config['SESSION_COOKIE_HTTPONLY'] = True # ป้องกัน JS เข้าถึง cookie
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax' # หรือ 'Strict' หรือ 'None' ขึ้นกับการใช้งาน
app.permanent_session_lifetime = timedelta(days=1) # กำหนดอายุของ session ตามต้องการ
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1) # ใช้ ProxyFix เพื่อรองรับการทำงานผ่าน proxy

# เพิ่มเติม Blueprint
app.register_blueprint(sample_Page)

# กำหนดค่า SocketIO
socketio.init_app(app)

# กำหนดเส้นทางหลัก
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
