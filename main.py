import os
import re

def parse_logs(log_file, keyword):
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(rf'\b{re.escape(keyword)}\b', line, re.IGNORECASE):
                yield line.strip()
def main():
    log_file = input("Enter the path to the log file: ")
    keyword = input("Enter the keyword to search for: ")    
    
    if not log_file or not keyword:
        print("Log file path and keyword cannot be empty.")
        return

    if os.path.exists(log_file):
        matches = parse_logs(log_file, keyword)
        for match in matches:
            for word in match.split():
                if word.lower() in keyword.lower().split():
                    print("\033[91m {}\033[00m".format(word), end=" ")
                else:
                    print(word, end=" ")
            print("")
    else:
         print("Log file not found.")

if __name__ == "__main__":
    main()
