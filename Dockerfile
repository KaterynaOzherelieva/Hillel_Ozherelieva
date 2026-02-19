FROM python:3.13.12

WORKDIR /app

COPY test_docker_database_conn.py .

RUN pip install pytest psycopg2-binary

CMD ["pytest", "-k", "TestDockerDB"]