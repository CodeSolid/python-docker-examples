import os
import sqlalchemy as sa

def get_connection_string(use_template=False) -> str:
    host = os.environ.get("POSTGRES_REMOTE_HOST")
    user = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    if use_template:
        db = "template1"
    else:
        db = os.environ.get("POSTGRES_DB")
    return f"postgresql+psycopg2://{user}:{password}@{host}/{db}"    

def connect(use_template=False, echo=True) -> sa.engine.base.Engine:
    return sa.create_engine(get_connection_string(use_template), echo=echo)

