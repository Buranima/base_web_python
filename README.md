# 🌐 ระบบเว็บแอปพลิเคชันด้วย Python

โปรเจกต์นี้เป็นระบบเว็บแอปที่พัฒนาโดยใช้ภาษา Python เหมาะสำหรับการเรียนรู้หรือใช้งานจริงในระบบภายใน เช่น API Server, Dashboard, IoT Monitoring, หรือ Web Control Panel

---

## 🔧 ความต้องการเบื้องต้น (Prerequisites)

- Python 3.12.10
- pip (ตัวจัดการแพ็กเกจ Python)
- Git (ถ้าจะโคลนจาก repo)
- เครื่องมือ IDE เช่น VS Code (แนะนำ) + copilot

---

## ⚙️ วิธีติดตั้งและใช้งาน

### สำหรับ Windows

1. สร้าง virtual environment
python -m venv venv

2. เปิดใช้งาน virtual environment
.\venv\Scripts\activate

3. อัพเดต pip
python.exe -m pip install --upgrade pip

4. ติดตั้งไลบรารีที่จำเป็น
pip install -r requirements.txt

5. รันโปรเจกต์
python main.py

6. หากต้องการเก็บแพ็คเกจและไลบรารี่ต่างๆ
pip freeze > requirements.txt

---

### สำหรับ Linux / macOS


1. สร้าง virtual environment
python3 -m venv venv

2. เปิดใช้งาน virtual environment
source venv/bin/activate

3. อัพเดต pip
python3 -m pip install --upgrade pip

4. ติดตั้งไลบรารี
pip install -r requirements.txt

5. รันโปรเจกต์
python3 main.py

6. หากต้องการเก็บแพ็คเกจและไลบรารี่ต่างๆ
pip freeze > requirements.txt

---

## 📂 โครงสร้างโปรเจกต์เบื้องต้น


โฟลเดอร์ที่เก็บโค้ดทั้งหมด/
├── main.py                 # ไฟล์หลักสำหรับรันระบบ
├── README.md               # ไฟล์แนะนำโปรเจกต์นี้
├── requirements.txt        # รายการไลบรารี
├── Dockerfile              # ไฟล์สำหรับสร้าง Docker image
├── docker-compose.yml      # ไฟล์สำหรับจัดการ container ด้วย Docker Compose
├── templates/              # แม่แบบ HTML
    ├── index.html          # หน้าแรก
    └── layout/             # แม่แบบหลัก
├── static/                 # ไฟล์สื่อที่ไม่เปลี่ยนแปลง เช่น CSS, JS, img
    ├── css/                # รวมไฟล์ CSS
    ├── js/                 # รวมไฟล์ js
    └── img/                # รวมไฟล์ img
├── view/                   # ส่วนแสดงผล
├── upload/                 # โฟลเดอร์สำหรับอัพโหลดไฟล์
├── venv/                   # Virtual environment
└── .env                    # เก็บข้อมูลลับ เช่น token

---

## 💡 คำแนะนำสำหรับผู้ใช้ใหม่

1. อย่าลืมรัน activate virtual environment ก่อนติดตั้งแพ็กเกจหรือรันแอป

2. ใช้ .env สำหรับข้อมูลลับ เช่น DATABASE, SECRET_KEY

3. ถ้าใช้ Git ควรมี .gitignore เพื่อไม่รวมไฟล์สำคัญ เช่น .env, venv/, *.pyc

---

## 🐋 คำแนะนำการใช้งาน Docker เบื้องต้น

Docker คือเครื่องมือที่ใช้สำหรับ "บรรจุแอปพลิเคชัน + dependency ทั้งหมด" ไว้ใน container (เหมือนกล่องแอปที่พกพาได้)

### ตัวอย่าง Dockerfile

1. ใช้ Python image
FROM python:3.12.10

2. กำหนด working directory
WORKDIR /app

3. คัดลอกไฟล์ไปไว้ใน container
COPY . /app

4. ติดตั้ง dependency
RUN pip install --no-cache-dir -r requirements.txt

5. เปิดพอร์ต
EXPOSE 5000

6. รันแอป
CMD ["python3", "main.py"]

### ตัวอย่าง docker-compose.yml

version: '3.8'
services:
  app:
    build: .
    container_name: my_app
    restart: always
    ports:
      - 8080:5000
    volumes:
        - ./templates:/app/templates
        - ./static:/app/static
        - ./view:/app/view
        - ./upload:/app/upload
    environment:
      - ipaddress=${ipaddress}
      - usernamedb=${usernamedb}
      - passworddb=${passworddb}
      - dbanme=${dbanme}
      - portdb=${portdb}
    command: ["python3", "main.py"]

### คำสั่ง Docker เบื้องต้น

1. ดู container ที่กำลังรัน
sudo docker ps

2. ดู images ที่มีอยู่
sudo docker images

3. ดู log ของ container
sudo docker logs "ชื่อ container หรือ ID"

4. ดู log แบบเรียลไทม์
sudo docker logs -f "ชื่อ container หรือ ID"

5. เข้าไปใน container
sudo docker exec -it "ชื่อ container หรือ ID" bash

6. เข้าไปใน container ด้วยสิทธิ์ root
docker exec -it --user root "ชื่อ container หรือ ID" bash

6. restart container
sudo docker restart "ชื่อ container หรือ ID"

7. start container
sudo docker start "ชื่อ container หรือ ID"

8. stop container
sudo docker stop "ชื่อ container หรือ ID"

9. ลบ container
sudo docker rm "ชื่อ container หรือ ID"

10. ลบ image
sudo docker rmi "ชื่อ image หรือ ID"

11. สร้างและรัน container ด้วย Docker Compose
sudo docker-compose up -d --build

12. สร้าง image จาก Dockerfile
sudo docker build -t "ชื่อ image" .

### Cloudflare Tunnel สำหรับเชื่อมต่อแอปผ่านโดเมนเนม

1. ติดตั้ง cloudflared
sudo apt update
sudo apt install cloudflared -y

ตรวจสอบว่าใช้ได้หรือไม่
cloudflared --version

2. ล็อกอินกับ Cloudflare Account
cloudflared tunnel login

ระบบจะเปิดเบราว์เซอร์ให้ล็อกอิน Cloudflare
แล้วให้คุณเลือกโดเมน (เช่น comeng-kbu.com)
หลังจากกดอนุญาต จะมีไฟล์ credentials ถูกสร้างไว้ที่ ~/.cloudflared/(UUID).json

3. สร้าง Tunnel ใหม่
cloudflared tunnel create (ชื่อ tunnel)

ผลลัพธ์จะได้ประมาณนี้
Tunnel credentials written to /home/admin_comeng/.cloudflared/(UUID).json
Created tunnel comeng-kbu with id (UUID)

4. สร้างไฟล์ config.yml
sudo nano /etc/cloudflared/config.yml

ใส่เนื้อหานี้
tunnel: comeng-kbu
credentials-file: /home/admin_comeng/.cloudflared/(UUID).json

ingress:
  - hostname: kbubot.comeng-kbu.com
    service: http://localhost:5005

  - service: http_status:404

ปรับ hostname กับ port ให้ตรงกับเว็บที่คุณต้องการเปิด
กด Ctrl + O, Enter, Ctrl + X เพื่อบันทึก

5. เชื่อม DNS โดเมนกับ Tunnel
cloudflared tunnel route dns comeng-kbu kbubot.comeng-kbu.com

Cloudflare จะสร้าง CNAME ให้อัตโนมัติ
ชี้ไปยัง (UUID).cfargotunnel.com

6. ทดสอบรัน Tunnel
cloudflared tunnel run comeng-kbu

จะเห็น log ประมาณนี้
INF Starting tunnel comeng-kbu
INF Connected to Cloudflare edge
INF Route established kbubot.comeng-kbu.com → http://localhost:5005

7. ตั้งค่าให้รันอัตโนมัติเมื่อบูตเครื่อง
sudo cloudflared service install
sudo systemctl enable cloudflared
sudo systemctl start cloudflared

ตรวจสอบสถานะ
sudo systemctl status cloudflared

ถ้าเห็น “active (running)” ถือว่าเรียบร้อย

8. ตรวจสอบ log / debug
sudo journalctl -u cloudflared -f

จะเห็นทุกการเชื่อมต่อแบบ realtime

9. หยุดบริการ
sudo systemctl stop cloudflared

---