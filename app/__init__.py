from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 初始化 SQLAlchemy
db = SQLAlchemy(app)

from app import routes
from app.models import User  # 导入模型

# 将 db 作为 app 的属性
app.db = db