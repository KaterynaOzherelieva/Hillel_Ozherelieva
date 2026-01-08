import os
import requests


BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "sticker.png")


class TestImageAPI:
    filename = None

    def test_upload_image(self):

        with open(IMAGE_PATH, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(f"{BASE_URL}/upload", files=files)

        image_url = response.json()["image_url"]
        TestImageAPI.filename = image_url.split("/")[-1]

        assert response.status_code == 201

    def test_get_image_url(self):

        response = requests.get(f"{BASE_URL}/image/{TestImageAPI.filename}", headers={"Content-Type": "text"})
        assert response.status_code == 200



    def test_delete_image(self):

        response = requests.delete(f"{BASE_URL}/delete/{TestImageAPI.filename}")
        assert response.status_code == 200



