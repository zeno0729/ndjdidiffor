import time

def display_file_with_delay(file_path, delay=2):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')  # Print the line without adding an extra newline
            time.sleep(delay)    # Wait for the specified delay

# Usage
file_path = 'text.text'  # Replace with your file path
display_file_with_delay(file_path, delay=2)  # Delay of 2 seconds