import json
import logging


def json_validate(json_string:str) -> bool:
    """
    Check if json string is valid
    """
    logging.basicConfig(
        filename="validation.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
    )

    try:
        json.loads(json_string)
        print("JSON valid")
        return True
    except json.JSONDecodeError as e:
        error_massage = "Invalid JSON"
        logging.error(error_massage)
        print(error_massage)
        return False


# with open("localizations_en.json", "r", encoding="utf-8") as file:
#     localizations_en_check = file.read()
# json_validate(localizations_en_check)
#
# with open("localizations_ru.json", "r", encoding="utf-8") as file:
#     localizations_ru_check = file.read()
# json_validate(localizations_ru_check)
#
# with open("login.json", "r", encoding="utf-8") as file:
#     login_check = file.read()
# json_validate(login_check)
#
# with open("swagger.json", "r", encoding="utf-8") as file:
#     swagger_check = file.read()
# json_validate(swagger_check)

def json_validate_file(file_path: str) -> bool:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return json_validate(content)

files = [
    "localizations_en.json",
    "localizations_ru.json",
    "login.json",
    "swagger.json"
]

for file_name in files:
    json_validate_file(file_name)

