import practices.re_module as rm

test_string = """
hello world
1123
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""

print("+ represents one or more characters")
pattern = r'Mr\s\w+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

print("find all the names in the string")
pattern = r'M[rs]s?\.?\s\w+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

print("find all the names in the string in an alternate way")
pattern = r'(Mr|Ms|Mrs)\.?\s\w+'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)