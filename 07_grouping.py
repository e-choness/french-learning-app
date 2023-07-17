import re_module as rm
import re

test_string = """
hello world
1123
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
eyin@gmail.com
python-pattern@yahoo.de
engineering-tech@my-domain.org
"""

print("Parsing the emails in the text")
pattern = r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.[a-z]+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

print("Parsing the emails in the text in an alternate pattern")
pattern = r'[a-zA-Z0-9-]+@[a-zA-Z-]+\.(com|de|org|net|edu)'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

print("() is used for grouping")
pattern = r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)'
pattern_comp = re.compile(pattern)
results = pattern_comp.finditer(test_string)
for r in results:
    print(r.groups())
    # print(results.group(1))
    # print(results.group(2))
    # print(results.group(3))

print("split() and sub() can also grouping string")

test_string = "123abc456789abc123ABC"

print("split() returns a list of substrings")
pattern = re.compile(r"[a-cA-C]{3}")
splitted = pattern.split(test_string)
print(splitted)

print("sub() replace the string with a substring.")
test_string = "hello world, you are the best world!"
pattern = re.compile(r"world")
subbed_string = pattern.sub("planet", test_string)
print(subbed_string)

print("let's parse urls")
urls = """
hello
2020-05-20
http://python-engineer.com
https://www.python-handson.org
http://www.pyeng.net
"""

print("\\2\\3 are the indexes of the group, if the group is optional and couldn't be found, the group will be returned as None.")
pattern = re.compile(r"https?://(w{3}\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)")
matches = pattern.finditer(urls)
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)