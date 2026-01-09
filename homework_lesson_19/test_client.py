import os
import requests
from requests import Response

from image_upload_func import image_upload


BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "sticker.png")


class TestImageAPI:
    # filename = None

    def test_upload_image(self):

        response: Response = image_upload()
        assert response.status_code == 201

    def test_get_image_url(self):

        response: Response = image_upload()

        image_url = response.json()["image_url"]
        filename = image_url.split("/")[-1]


        response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})

        assert response.status_code == 200
        assert "json" in response.headers["Content-Type"]



    def test_get_image(self):

        response: Response = image_upload()

        image_url = response.json()["image_url"]
        filename = image_url.split("/")[-1]


        response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "image"})

        with open('test_image_download.png', 'wb') as image:
            image.write(response.content)

        assert response.status_code == 200
        assert "image" in response.headers["Content-Type"]



    def test_delete_image(self):

        response: Response = image_upload()

        image_url = response.json()["image_url"]
        filename = image_url.split("/")[-1]


        response = requests.delete(f"{BASE_URL}/delete/{filename}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/image/{filename}", headers={"Content-Type": "text"})
        assert response.status_code == 404



