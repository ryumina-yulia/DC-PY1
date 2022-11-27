import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as f:
        headers = f.readline()[:-1].split(delimiter)
        rows = [line[:-1].split(delimiter) for line in f.readlines()]
        return [dict(zip(headers, line)) for line in rows]




print(json.dumps(csv_to_list_dict(INPUT_FILE),indent=4))
