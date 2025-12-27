import logging
import xmltodict


def find_incoming_by_group_number(xml_file: str, group_number: str):
    """
    Search for a group by number and logs timingExbytes/incoming value.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("groups_logger")

    with open(xml_file, "r", encoding="utf-8") as file:
        data = xmltodict.parse(file.read())

    groups = data["groups"]["group"]

    for group in groups:
        number = group.get("number")

        if number == group_number:
            timing = group.get("timingExbytes")

            if timing and "incoming" in timing:
                incoming = timing["incoming"]
                logger.info(
                    f"Group {group_number}: timingExbytes/incoming = {incoming}"
                )
                return

            else:
                logger.info(
                    f"Group {group_number} does not have timingExbytes/incoming"
                )
                return


find_incoming_by_group_number("groups.xml", "0")