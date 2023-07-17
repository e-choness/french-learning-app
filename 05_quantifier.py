import re_module as rm

test_string = "hello_123"

# Putting * after the pattern enables the search for all characters in that pattern.
print("Putting * after the pattern enables the search for all characters in that pattern.")
pattern = r'\d*'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# Putting * after the pattern enables the search for all continuous characters in that pattern.
print("Putting + after the pattern enables the search for all continuous characters in that pattern.")
pattern = r'\d+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# Putting ? after the pattern enables the search for pattern may or may not exist.
print("Putting ? after the pattern enables the search for pattern may or may not exist.")
pattern = r'_?\d+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# Putting {number} will find the exact number of matches 
print("Putting {number} will find the exact number of matches.")
pattern = r'\d{1,2}'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

dates = """
hello
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
"""

print("let's parse some dates")

pattern = r'\d{4}.\d{2}.\d{2}'
results = rm.find_matches_iter(dates, pattern)
rm.print_result(results)

print("find format with -")
pattern = r'\d{4}-\d{2}-\d{2}'
results = rm.find_matches_iter(dates, pattern)
rm.print_result(results)

print("find format with -, / and _")
pattern = r'\d{4}[-/_]\d{2}[-/_]\d{2}'
results = rm.find_matches_iter(dates, pattern)
rm.print_result(results)

print("find May to July")
pattern = r'\d{4}[-/_]0[5-7][-/_]\d{2}'
results = rm.find_matches_iter(dates, pattern)
rm.print_result(results)