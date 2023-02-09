#
# @add_user.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv


load_dotenv()
Base = declarative_base()

url = getenv("URL_DB")
print(url)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

engine = create_engine('mysql+pymysql://root@localhost/converter_db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = User(user_name="converter_user", password="1234")
user2 = User(user_name="denisse", password="12345")
session.add(user)
session.add(user2)
session.commit()

users = session.query(User).all()
print([user.user_name for user in users])

