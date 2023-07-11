from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DDL
from sqlalchemy.ext.declarative import declarative_base



conn_str = 'clickhouse://default:@localhost/default'
engine = create_engine(conn_str)
session = sessionmaker(bind=engine)

Base = declarative_base()


database = 'test'
engine.execute(DDL(f'CREATE DATABASE IF NOT EXISTS {database}'))