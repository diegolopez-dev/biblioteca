from sqlalchemy import MetaData, create_engine

engine = create_engine("mysql+pymysql://root@localhost:3306/libros")

meta_data = MetaData()

