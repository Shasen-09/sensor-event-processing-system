import psycopg


class Database:
    def __init__(self):
        self.connection = psycopg.connect(
            host="localhost",
            port=5432,
            dbname="TRACK",
            user="postgres",
            password="shasen"
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
