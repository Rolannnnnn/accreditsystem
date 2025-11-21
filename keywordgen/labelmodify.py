import json

inputjson = "jsons/grades1.json"
outputjson = "output.json"

fromlabel = "grades of sheet"
tolabel = "gradesofsheet"

def fix_labels(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        if item.get("label") == fromlabel:
            item["label"] = tolabel

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    fix_labels(inputjson, outputjson)