# 之前定義的 basedir (要修正為 BASE_DIR)
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-should-change-this'

    # --- 修改這裡 ---
    # 直接讀取環境變數，如果 Render 上沒設定好，就讓它直接報錯，這是正確的行為
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # 為了安全，你可以加上一個檢查，如果沒讀到就拋出錯誤
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("No SQLALCHEMY_DATABASE_URI set for the application")
    # --- 修改結束 ---

    SQLALCHEMY_TRACK_MODIFICATIONS = False
