from logging_functions import log_event, get_last_log

LOG_PATH = "logs.log"

class TestLogEvent:

    def test_log_event_success_status(self):
        test_username = "Olga"
        test_status = "success"
        test_data = {"username": test_username, "status": test_status}

        log_event(**test_data)
        last_log: str = get_last_log(LOG_PATH)


        actual_level = last_log.split()[3]
        actual_username = last_log.split("Username: ")[1].split(",")[0]
        actual_status = last_log.split("Status: ")[1].strip()

        assert actual_level == "INFO"
        assert actual_username == test_username
        assert actual_status == test_status

    def test_log_event_expired_status(self):
        test_username = "Ivan"
        test_status = "expired"
        log_event(test_username, test_status)
        last_log = get_last_log(LOG_PATH)

        actual_level = last_log.split()[3]
        actual_username = last_log.split("Username: ")[1].split(",")[0]
        actual_status = last_log.split("Status: ")[1].strip()

        assert actual_level == "WARNING"
        assert actual_username == test_username
        assert actual_status == test_status

    def test_log_event_else_status(self):
        test_username = "Unknown"
        test_status = "wrong_password"
        log_event(test_username, test_status)
        last_log = get_last_log(LOG_PATH)

        actual_level = last_log.split()[3]
        actual_username = last_log.split("Username: ")[1].split(",")[0]
        actual_status = last_log.split("Status: ")[1].strip()

        assert actual_level == "ERROR"
        assert actual_username == test_username
        assert actual_status == test_status