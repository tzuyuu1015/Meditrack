from app import create_app, db
# 1. 在這裡匯入你所有的模型！
from app.models import User, Patient, VitalSign, LabResult 
from werkzeug.security import generate_password_hash
import os
from seed_demo import seed_demo_data 

app = create_app()

# 應用程式啟動時，自動執行所有檢查
with app.app_context():
    db.create_all() # 確保所有資料表都已建立
    
    # 檢查並建立 admin 帳號
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            role="admin",
            password_hash=generate_password_hash("admin123")
        )
        db.session.add(admin)
        db.session.commit()
        print(">> Seeded default admin (username=admin, password=admin123)")
    
    # 檢查並填充範例病患資料
    if Patient.query.first() is None:
        print(">> 偵測到病患資料庫為空，正在執行初始資料填充...")
        seed_demo_data() # 執行你的 seeding 函數
        print(">> Demo 資料填充完畢！")
    else:
        print(">> 偵測到已有病患資料，跳過初始資料填充。")


if __name__ == "__main__":
    app.run(debug=True)

