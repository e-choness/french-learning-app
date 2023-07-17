import re_module as rm

text_string = "123abc456789abc123ABC."

# Without escacpe, . parses string as the same as split() function
print("Without escacpe, . parses string as the same as split() function")
pattern_string = r"."
results = rm.find_all_matches(text_string, pattern_string)
rm.print_result(results)

# With escape, it looks for . character in the string
print("With escape, it looks for . character in the string")
pattern_string = r"\."
results = rm.find_all_matches(text_string, pattern_string)
rm.print_result(results)

# ^ is for searching from the beginning
print("^ is for searching from the beginning")
pattern_string = r"^123"
results = rm.find_all_matches(text_string, pattern_string)
rm.print_result(results)

# $ is for searching the substring at the end
print("^ is for searching from the beginning")
pattern_string = r"ABC.$"
results = rm.find_all_matches(text_string, pattern_string)
rm.print_result(results)