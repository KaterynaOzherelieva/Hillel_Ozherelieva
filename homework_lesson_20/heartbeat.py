import logging
from datetime import datetime, timedelta



logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s %(asctime)s %(message)s"
)


def read_log_file(filename):
    """
    Reading lines from hblog.txt
    """
    with open(filename, "r") as f:
        return f.readlines()



def filter_by_key(lines, key):
    """
    Filter lines by KEY
    """
    filtered_lines = []
    for line in lines:
        if key in line:
            filtered_lines.append(line)
    return filtered_lines


def extract_timestamp(line):
    """
    Finding timestamps
    """
    keyword_index = line.find("Timestamp ")
    time_str = line[keyword_index + len("Timestamp ") : keyword_index + len("Timestamp ") + 8]
    return datetime.strptime(time_str, "%H:%M:%S")


def analyze_heartbeat(filtered_lines):
    """
    Checking & logging timestamp difference
    """
    for i in range(len(filtered_lines) - 1):
        t1 = extract_timestamp(filtered_lines[i])
        t2 = extract_timestamp(filtered_lines[i + 1])

        diff = abs((t2 - t1).total_seconds())

        massage = f"heartbeat = {int(diff)} sec between {t1.time()} and {t2.time()}"

        if 31 < diff < 33:
            logging.warning(massage)

        if diff >= 33:
            logging.error(massage)



def main():
    key = "Key TSTFEED0300|7E3E|0400"
    lines = read_log_file("hblog.txt")
    filtered = filter_by_key(lines, key)
    analyze_heartbeat(filtered)


if __name__ == "__main__":
    main()

