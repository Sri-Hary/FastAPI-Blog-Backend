from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = "mysql+pymysql://user-name:passowrd:port/blogapplication"


engine = create_engine(
    URL_DATABASE,
    pool_pre_ping=True
)


sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


base = declarative_base()
