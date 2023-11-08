import re

# Regular expressions for parsing log lines
log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+): (.+)'
error_pattern = r'(error|exception|failed)'
warning_pattern = r'(warning|alert)'

# Function to parse log lines and correlate events


def process_log_line(line):
    match = re.match(log_pattern, line)
    if match:
        timestamp, log_level, message = match.groups()
        if re.search(error_pattern, message, re.IGNORECASE):
            print(f'Error Event: {timestamp} - {message}')
        elif re.search(warning_pattern, message, re.IGNORECASE):
            print(f'Warning Event: {timestamp} - {message}')
        else:
            print(f'Info Event: {timestamp} - {message}')
    else:
        print(f'Unrecognized Log Format: {line}')


# Log capturing loop (reads from standard input)
print('Enter logs (press Ctrl + D to end input):')
try:
    while True:
        log_line = input()
        process_log_line(log_line)
except EOFError:
    print('Log input ended.')
