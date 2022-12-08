from sqlalchemy import MetaData, Table, Column, Integer, String
import connection as conn
# JCL TODO Should be true ultimately
engine = conn.connect(use_template=False)

meta = MetaData()
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

if __name__ == "__main__":
    
    meta.create_all(engine)