log_file = open("log.txt", "r")
output = open("output.txt", "w")

search_term = "getTransport: Cannot find entry"

reviewed_lines = set()

# Scrape and check for duplicate entry
for line in log_file:
    if search_term in line:
        line_splitted = line[line.index("getTransport"):]
        if line_splitted not in reviewed_lines:
            reviewed_lines.add(line_splitted)
            output.write(line_splitted)