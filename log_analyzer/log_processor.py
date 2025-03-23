import re

# Regex pattern to extract timestamp, user ID, log level, and message
LOG_PATTERN = re.compile(
    r"\[(.*?)\] \[User:\s(\d+)\] (ERROR|WARNING|INFO): (.+)"
)

def read_log_file(file_path):
    """Generator to read the log file line by line (memory efficient)."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def extract_log_data(log_line):
    """Extract log details using regex."""
    match = LOG_PATTERN.search(log_line)
    if match:
        return {
            "timestamp": match.group(1),
            "user_id": match.group(2),
            "log_level": match.group(3),
            "message": match.group(4)
        }
    return None
