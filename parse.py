import re
import json

def transform_urls(input_filename, output_filename):
    url_pattern = r'\[([^\]]+)\]\s+([^\s]+)'

    with open(input_filename, 'r') as input_file:
        input_lines = input_file.readlines()

    output_list = []

    for line in input_lines:
        match = re.match(url_pattern, line)
        if match:
            name = match.group(1)
            url = match.group(2)
            url_type = "Replit" if "repl.co" in url else "Web/Online"

            if "repl.co" in url:
                full_url = f"https://replit.com/@{name}"
            else:
                full_url = url

            output_list.append({
                "name": name,
                "url": full_url,
                "type": url_type
            })

    with open(output_filename, 'w') as output_file:
        json.dump(output_list, output_file, indent=4)

if __name__ == "__main__":
    input_filename = "sub.txt"  # Change this to your input filename
    output_filename = "sub.json"  # Change this to your output filename
    transform_urls(input_filename, output_filename)