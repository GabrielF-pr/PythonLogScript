import os
import re
import sys

def parse_logs(log_file, keyword):
    with open(log_file, 'r') as file:
        for line in file:
            line_lower = line.lower()
            for key in keyword:
                if re.search(rf'\b{re.escape(key)}\b', line_lower, re.IGNORECASE):
                    yield re.sub(rf"\b{key}\b", lambda m: f"\033[91m {m.group(0)}\033[00m", line.lower())

def save_to_file(matches, keyword):
    with open("matches.log", 'w') as file:
        for line_num, match in enumerate(matches, start=1):
            file.write(f"\x1b[1;32m[Line {line_num}]\x1b[0m")
            file.write(match)

def print_screen(matches, keyword):
    for line_num, match in enumerate(matches, start=1):
        print(f"\x1b[1;32m[Line {line_num}]\x1b[0m", end="")
        print(match)

def print_help():
    print("Provide a valid file and enter a keyword you would like to find within the file.")
    print("Then, decide whether you want to save it to a file or print it to the screen.")

def check_arguments():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print_help()
            return

def main():
   
    log_file = input("Enter the path to the log file: ").strip()
    keyword = input("Enter the keyword to search for: ").strip()    
    save_file = input("Would you like to save the output into a file? (yes/no): ").strip()
    
    if not log_file or not keyword:
        print("Log file path and keyword cannot be empty.")
        return
    
    if not os.path.isfile(log_file):
        print("Provided path is not a valid file.")
        return
    
    if os.path.exists(log_file):
        keyword = keyword.split(",")
        matches = parse_logs(log_file, keyword)
        if save_file == "yes":
            save_to_file(matches, keyword)
            return
        print_screen(matches, keyword)
    else:
         print("Log file not found.")

if __name__ == "__main__":
    main()
