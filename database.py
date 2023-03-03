from sqlalchemy import create_engine, text

import os


database_uri = os.environ.get("DB_CONNECTION_STRING")
engine = create_engine(database_uri, connect_args=
                       {
                           'ssl': {'ssl_ca': "/etc/ssl/cert.pem"}
                        })



def load_jobs_from_db():
    with engine.connect() as con:
        rs = con.execute(text("SELECT * FROM jobs"))
        return rs.fetchall()