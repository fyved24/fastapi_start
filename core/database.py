from sqlmodel import SQLModel, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# 创建数据库引擎
engine = create_engine(sqlite_url, pool_pre_ping=True)
