import pytest
import logging
import allure

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("brand", 10),
        ("engine_volume", 7),
        ("price", 1),
        (None, 5),
    ]
)

@allure.title("Cars API search")
class TestCarsSearch:
    """
    Test content getting, flask server should return 200 status code and content in response for cars with such params (sort_by, limit):
        price, 5,
        year, 3,
        brand, 10,
        engine_volume, 7,
        price, 1,
        None, 5
    """

    def test_search_cars(self, auth_session, sort_by, limit):
        logger.info(f"TEST: sort_by={sort_by}, limit={limit}")

        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = auth_session.get(
            "http://127.0.0.1:8080/cars",
            params=params
        )

        with allure.step("Test checks"):
            assert response.status_code == 200
            data = response.json()

            if limit:
                assert len(data) <= limit