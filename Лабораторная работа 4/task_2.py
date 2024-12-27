import json
json_file = "input.json"
def task() -> float:
    with open(json_file) as j:
        file = json.load(j)
    sum_ = sum([item["score"] * item["weight"] for item in file])
    return round(sum_, 3)


print(task())
