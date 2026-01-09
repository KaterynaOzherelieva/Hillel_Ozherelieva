import requests
import os

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "sticker.png")

def image_upload():
    with open(IMAGE_PATH, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(f"{BASE_URL}/upload", files=files)

        # image_url = response.json()["image_url"]
    return response