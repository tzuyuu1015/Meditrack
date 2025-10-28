from app import create_app, db
from app.models import User, Patient  # <-- 1. 在這裡多匯入 Patient
from werkzeug.security import generate_password_hash
import os
from seed_demo import seed_demo_data  # <-- 2. 從 seed_demo 匯入我們的新函數

app = create_app()

# 第一次啟動自動建 DB、建立管理者、並填充範例資料
with app.app_context():
    db.create_all()  # 建立所有表格
    
    # 3. 檢查並建立 admin
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            role="admin",
            password_hash=generate_password_hash("admin123")
        )
        db.session.add(admin)
        db.session.commit()
        print(">> Seeded default admin (username=admin, password=admin123)")
    
    # 4. 檢查並填充範例病患資料 (把你的新邏輯移到這裡)
    if Patient.query.first() is None:
        print(">> 資料庫是空的，正在執行初始資料填充...")
        seed_demo_data()  # 執行你的 seeding 函數
        print(">> 資料填充完畢！")

if __name__ == "__main__":
    app.run(debug=True)
