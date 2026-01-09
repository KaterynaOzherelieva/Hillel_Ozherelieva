import requests

from requests import Response

BASE_URL = "https://images-api.nasa.gov"


search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response: Response = requests.get(search_url, params=search_params)
search_data = response.json()

# print(search_data)


items = search_data["collection"]["items"]

item_id_1 = items[0]["data"][0]["nasa_id"]
item_id_2 = items[1]["data"][0]["nasa_id"]

asset_url_1 = f"{BASE_URL}/asset/{item_id_1}"
asset_url_2 = f"{BASE_URL}/asset/{item_id_2}"

asset_1_response: Response = requests.get(asset_url_1).json()
asset_2_response: Response = requests.get(asset_url_2).json()

url_list_1 = asset_1_response["collection"]["items"]
url_list_2 = asset_2_response["collection"]["items"]

def find_image(url_lists):
    for url in url_lists:
        if url["href"].endswith(".jpg"):
            return url["href"]

jpg_url_1 = find_image(url_list_1)
jpg_url_2 = find_image(url_list_2)

image_1 = requests.get(jpg_url_1)
image_2 = requests.get(jpg_url_2)

with open("nasa_image_1.jpg", "wb") as file:
    file.write(image_1.content)

with open("nasa_image_2.jpg", "wb") as file:
    file.write(image_2.content)