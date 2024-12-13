import os
import re

def parse_logs(log_file, keyword):
    results = []
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(keyword, line):
                results.append(line.strip())
    return results

def main():
    log_file = input("Enter the path to the log file: ")
    keyword = input("Enter the keyword to search for: ")    
    
    if os.path.exists(log_file):
        matches = parse_logs(log_file, keyword)
        print(f"Found {len(matches)} matching lines:")
        for match in matches:
            print(match)
    else:
         print("Log file not found.")

if __name__ == "__main__":
    main()