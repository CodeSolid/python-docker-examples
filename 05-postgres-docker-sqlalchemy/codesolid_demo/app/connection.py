import os
import sqlalchemy as sa

def get_connection_string() -> str:
    host = os.environ.get("POSTGRES_REMOTE_HOST")
    user = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    db = os.environ.get("POSTGRES_DB")
    return f"postgresql+psycopg2://{user}:{password}@{host}/{db}"    

def connect() -> sa.engine.base.Engine:
    return sa.create_engine(get_connection_string())

