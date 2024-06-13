from sqlalchemy import MetaData, create_engine

engine = create_engine("mysql+pymysql://ukyzejr0hs2cx5jx:8rvC8MWKr78bwNIZRnYQ@bjzsvhqj46svlfmaydpn-mysql.services.clever-cloud.com:3306/bjzsvhqj46svlfmaydpn")

meta_data = MetaData()

