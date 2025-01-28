import csv

def get_dataset(archive):
    data = []
    with open(archive, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data.append({key: float(value) if key != "id" else int(value) for key, value in row.items()})

    return data
