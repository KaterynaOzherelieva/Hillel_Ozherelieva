import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"


    logging.basicConfig(
        filename='logs.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )

    logger = logging.getLogger("log_event")


    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


def get_last_log(filepath: str):
    """
    Зчитує останній запис з лог-файлу
    """
    with open(filepath, "r") as file:
        lines = file.readlines()
    return lines[-1] if lines else ""
