
import csv

location_corrupted: str = "sales_export.csv"
location_recovered: str = "sales_export_rec.csv"

s1: list[dict] = []
s2: list[dict] = []
s3: list[dict] = []
s4: list[dict] = []
s_exception: list[dict] = []

def open_corrupted(location_corrupted: str):
    with open(location_corrupted, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            if row["store_id"] == 'S01':
                clean_row(row)
                s1.append(row)

            elif row["store_id"] == 'S02':
                s2.append(row)
            elif row["store_id"] == 'S03':
                s3.append(row)
            elif row["store_id"] == 'S04':
                s4.append(row)
            else:
                s_exception.append(row)

with open("sales_export_rec.csv", "w", encoding="utf-8") as file:
    file.write("New content\n")

def clean_row(row):
    print("wip")

    while True:
        open_corrupted(location_corrupted)
        print("####################################")
        print(s1)
        print("####################################")
        print(s2)
        print("####################################")
        print(s3)
        print("####################################")
        print(s4)
        print("####################################")
        print(s_exception)
        break
