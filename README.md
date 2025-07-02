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
├── templates/              # แม่แบบ HTML (หากใช้ Flask)
    ├── index.html          # หน้าแรก
    └── layout/             # แม่แบบหลัก
├── static/                 # ไฟล์สื่อที่ไม่เปลี่ยนแปลง เช่น CSS, JS, img
    ├── css/                # รวมไฟล์ CSS
    ├── js/                 # รวมไฟล์ js
    └── img/                # รวมไฟล์ img
├── view/                   # ส่วนแสดงผล (หากใช้ Flask)
├── venv/                   # Virtual environment
└── .env                    # เก็บข้อมูลลับ เช่น token

---

## 💡 คำแนะนำสำหรับผู้ใช้ใหม่

1. อย่าลืมรัน activate virtual environment ก่อนติดตั้งแพ็กเกจหรือรันแอป

2. ใช้ .env สำหรับข้อมูลลับ เช่น DATABASE, SECRET_KEY

3. ถ้าใช้ Git ควรมี .gitignore เพื่อไม่รวมไฟล์สำคัญ เช่น .env, venv/, *.pyc

---