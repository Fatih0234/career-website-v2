from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()

database_uri = os.getenv("api_key")
engine = create_engine(database_uri, connect_args=
                       {
                           'ssl': {'ssl_ca': "/etc/ssl/cert.pem"}
                        })



def load_jobs_from_db():
    with engine.connect() as con:
        rs = con.execute(text("SELECT * FROM jobs"))
        return rs.fetchall()