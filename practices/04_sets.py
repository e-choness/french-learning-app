import practices.re_module as rm

test_string = "helloHELLO 123-_"

# [] contains all the single characters to be found
print("[] contains all the single characters to be found")
pattern = r'[helo]'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)

# [] contains all the single characters to be found
print("a-z A-Z 0-9 _ are the ranges of matching characters")
pattern = r'[a-z0-9-]'
results = rm.find_matches_iter(test_string, pattern)
rm.print_result(results)
