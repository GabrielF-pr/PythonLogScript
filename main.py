import os
import re

def parse_logs(log_file, keyword):
    with open(log_file, 'r') as file:
        for line in file:
            if re.search(rf'\b{re.escape(keyword)}\b', line, re.IGNORECASE):
                yield line.strip()

def save_to_file(matches, keyword):
    with open("matches.log", 'w') as file:
        for line_num, match in enumerate(matches, start=1):
            file.write(f"\x1b[1;31m[Line {line_num}]\x1b[0m")
            for word in match.split():
                if word.lower() in keyword.lower().split():
                    file.write(f"\033[91m {word}\033[00m")
                else:
                    file.write(f" {word} ")
            file.write('\n')

def main():
    log_file = input("Enter the path to the log file: ")
    keyword = input("Enter the keyword to search for: ")    
    save_file = input("Would you like to save the output into a file? (yes/no): ")
    
    if not log_file or not keyword:
        print("Log file path and keyword cannot be empty.")
        return
    
    if os.path.exists(log_file):
        matches = parse_logs(log_file, keyword)
        if save_file == "yes":
            save_to_file(matches, keyword)
            return

        for line_num, match in enumerate(matches, start=1):
            print(f"\x1b[1;31m[Line {line_num}]\x1b[0m", end="")
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
