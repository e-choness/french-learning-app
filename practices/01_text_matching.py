import practices.re_module as rm

test_string = '123abc456789abc123ABC'

# This is an alternate way to write regex. Same result.
# matches = rm.finditer(test_string, r"abc")
# rm.print_result(matches)

# match() only finds the first match from the string beginning
# If no match at the beginning, it will return None.
# split() and sub() can be used to modify the string
match = rm.find_matches(test_string, r"123")
rm.print_result(match)

# findall() will find all matched strings 
results = rm.find_all_matches(test_string, r"abc")
rm.print_result(results)

# finditer() will find all matched strings and their indexes
# group(), start(), end(), span() can be used on iterators
# span() gets the tuple of the matched string begin and end indexes
results = rm.find_matches_iter(test_string, r"abc")
rm.print_result(results)