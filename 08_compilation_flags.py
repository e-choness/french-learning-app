import re

my_string = "Hello World"
pattern = re.compile(r"world", re.IGNORECASE)
matches = pattern.finditer(my_string)
for match in matches:
    print(match)