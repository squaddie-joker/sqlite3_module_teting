import os
from sqlalchemy import create_engine

engine = create_engine('sqlite:///D:\\python_work\\sqlAlchemy_test\\test_db.db')
engine.connect()

print(engine)