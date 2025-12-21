import csv

unique_rows = []
seen_rows = set()


with open("rmc.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")

    for row in reader:
        row_tuple = tuple(row)

        if row_tuple not in seen_rows:
            seen_rows.add(row_tuple)
            unique_rows.append(row)


with open("r-m-c.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")

    for row in reader:
        row_tuple = tuple(row)

        if row_tuple not in seen_rows:
            seen_rows.add(row_tuple)
            unique_rows.append(row)


with open("result.csv", "w", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerows(unique_rows)
