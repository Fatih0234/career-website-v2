from sqlalchemy import create_engine, text

import os


database_uri = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(database_uri, connect_args=
                       {
                           'ssl': {'ssl_ca': "/etc/ssl/cert.pem"}
                        })


def load_jobs_from_db():
    with engine.connect() as con:
        rs = con.execute(text("SELECT * FROM jobs"))
        jobs = []
        
        for row in rs.all():
            jobs.append(row._asdict())

    return jobs


def load_job_from_db(job_id):
    with engine.connect() as con:
        rs = con.execute(text("SELECT * FROM jobs WHERE id=:id"), {"id": job_id})
        job = rs.first()._asdict()
    return job
    