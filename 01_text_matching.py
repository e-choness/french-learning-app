import re_module as rm

test_string = '123abc456789abc123ABC'

# This is an alternate way to write regex. Same result.
# matches = rm.finditer(test_string, r"abc")
# rm.print_result(matches)

# match() only finds the first match from the string beginning
# If no match at the beginning, it will return None.
match = rm.find_matches(test_string, r"123")
rm.print_result(match)

# find_all_matches() will find all match strings and their locations
results = rm.find_all_matches(test_string, r"abc")
rm.print_result(results)