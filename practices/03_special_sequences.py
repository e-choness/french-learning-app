import practices.re_module as rm

test_string = "hello 123_ heyho hohey"

# \d for any digit characters
print("\d for any digit characters")
pattern = r"\d"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# \D for any non-digit characters
print("\D for any non-digit characters")
pattern = r"\D"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# \s for any whitespace characters
print("\s and \W for any whitespace characters")
pattern = r"\s"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# \S for any non-whitespace characters
print("\S and \w for any non-whitespace characters")
pattern = r"\S"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# \b for substrngs begining with the pattern
print("\\b for substrngs begining with the pattern")
pattern = r"\bhey"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# \B for substrngs end with the pattern
print("\B for substrngs end with the pattern")
pattern = r"\Bhey"
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)