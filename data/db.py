import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.connection = psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )

    def save_event(self, event):
        with self.connection.cursor() as cur:
            cur.execute(
                """
        INSERT INTO events(sensor_id,value,timestamp)
        VALUES(%s,%s,%s)
        """, (
                    event.sensor_id,
                    event.value,
                    event.timestamp,
                )
            )
        self.connection.commit()

    def close(self):
        self.connection.close()
