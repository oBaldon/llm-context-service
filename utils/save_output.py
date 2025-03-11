import os
import json

def save_as_json(result, filename="output"):
    os.makedirs("temp", exist_ok=True)
    path = os.path.join("temp", f"{filename}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    return path

def save_as_txt(result, filename="output"):
    os.makedirs("temp", exist_ok=True)
    path = os.path.join("temp", f"{filename}.txt")

    assistant_response = ""
    if isinstance(result, list):
        for entry in result:
            if entry.get("role") == "assistant":
                assistant_response += entry.get("content", "") + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(assistant_response.strip())

    return path