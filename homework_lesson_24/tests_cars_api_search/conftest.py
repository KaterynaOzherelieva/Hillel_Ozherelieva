import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("test_search.log")
    ]
)

logger = logging.getLogger(__name__)



@pytest.fixture(scope="class")
def auth_session():
    logger.info("AUTH: start authentication")

    session = requests.Session()

    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200

    access_token = response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    logger.info("AUTH: success")

    yield session

    logger.info("AUTH: closing session")
    session.close()