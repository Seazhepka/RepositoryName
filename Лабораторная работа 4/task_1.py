import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    jsonArray = []
    with open(INPUT_FILENAME, encoding='utf-8') as f:
        csv_f = csv.DictReader(f)
        for row in csv_f:
            jsonArray.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as j:
        j.write(json.dumps(jsonArray, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
