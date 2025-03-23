from log_processor import read_log_file, extract_log_data
from decorators import log_errors, time_tracker
from utils.file_handler import save_logs_to_json

LOG_FILE_PATH = "logs/server_logs.txt"

@log_errors
@time_tracker
def process_logs():
    """Reads log file, extracts data, and saves it to JSON."""
    logs = []
    for line in read_log_file(LOG_FILE_PATH):
        log_data = extract_log_data(line)
        if log_data:
            logs.append(log_data)
    
    if logs:
        save_logs_to_json(logs)

# Run the log analyzer
if __name__ == "__main__":
    process_logs()
