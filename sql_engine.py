import sqlalchemy
from datetime import datetime

class NoDatabaseError(Exception):
    pass

class GresEngine:

    def __init__(self):
        with open("db_secret", "r") as f:
            DB_SECRET = f.read().strip()
        # Example connection string for local Postgres
        # Format: postgresql+psycopg2://user:password@localhost:5432/dbname
        self.local_pg_url = f"postgresql+psycopg2://postgres:{DB_SECRET}@localhost:5432/postgres"
        self.engine = sqlalchemy.create_engine(self.local_pg_url)
        print("SQLAlchemy engine created with URL:", self.local_pg_url)
        self.connection = self.connect()

    def connect(self):
        self.connection = self.engine.connect()
        print("Connected to the database.")
        return self.connection
    
    def close(self):
    
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            print("Not connected")
            raise NoDatabaseError("No active database connection to close.")
    
    def write_instance(self):
        self.connection.execute(sqlalchemy.text(
            "INSERT INTO foon.fooninstances (record_source, created_at) VALUES ('phone_proximity', :now)"),
            {"now": datetime.now().isoformat() } )
        self.connection.commit()

    def write_heartbeat(self, detector: str):
        now = datetime.now()
        self.connection.execute(sqlalchemy.text(
            "INSERT INTO foon.foondetectheartbeat (record_source, heartbeat_time) VALUES (:detector, :now)"), 
            {"detector": detector,"now": now})
        self.connection.commit()
