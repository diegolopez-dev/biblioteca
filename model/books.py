from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import engine, meta_data

books = Table("books", meta_data, 
            Column("id", Integer, primary_key=True),
            Column("name", String(255), nullable=False),
            Column("autor", String(255), nullable=False),
            Column("rating", Float, nullable=False)
        )

meta_data.create_all(engine)