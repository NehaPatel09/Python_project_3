import json

def save_logs_to_json(logs, output_file="logs/processed_logs.json"):
    """Save extracted logs into a JSON file."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)
    print(f"Logs saved successfully to {output_file}")
