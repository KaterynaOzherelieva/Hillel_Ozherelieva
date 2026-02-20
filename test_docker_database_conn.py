import psycopg2

class TestDockerDB:
    def test_docker_db_container_connection(self):
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="db",
            port="5432"
        )
        assert conn is not None

    def test_data_insertion(self):
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="db",
            port="5432"
        )
        cursor = conn.cursor()



        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100))")

        cursor.execute("INSERT INTO users (name) VALUES ('John')")
        conn.commit()

        cursor.execute("SELECT * FROM users WHERE name='John'")
        result = cursor.fetchone()
        assert result[1] == 'John'

        cursor.close()
        conn.close()