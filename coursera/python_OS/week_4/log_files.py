## !/usr/bin/env python3

# import sys

# logfile = sys.argv[1]
# with open(logfile) as f:
#     for line in f:
#         if "CORN" not in line:
#             continue
#         print(line.strip())
        
        
import re
#\[(\w+)\]
#(^\w+\s+\w+\s+\d+\s\d+:\d+:\d+)
pattern = r"(^\w+\s+\w+\s+\d+\s\d+:\d+:\d+) \[(\d+)\]"
line = "jul 6 4 14:04:01 computer.name CORN[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result)


