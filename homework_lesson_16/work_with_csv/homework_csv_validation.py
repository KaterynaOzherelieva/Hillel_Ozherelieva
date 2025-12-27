import csv

rows = set()


with open("rmc.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")

    for row in reader:
        rows.add(tuple(row))



with open("r-m-c.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")

    for row in reader:
        rows.add(tuple(row))



with open("result.csv", "w", encoding="utf-8") as out:
    writer = csv.writer(out)
    for row in rows:
        writer.writerow(row)
