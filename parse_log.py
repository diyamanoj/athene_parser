log_file = open("log.txt", "r")
output = open("output.txt", "w")

search_term = "getTransport: Cannot find entry"

for line in log_file:
    if search_term in line:
        output.write(line)