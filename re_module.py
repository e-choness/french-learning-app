import re

def find_matches(sample_text, pattern_string):
    pattern = re.compile(pattern_string)
    matches = pattern.match(sample_text)

    return matches

def find_searches(sample_text, pattern_string):
    pattern = re.compile(pattern_string)
    searches = pattern.search(sample_text)

    return searches

def find_all_matches(sample_text, pattern_string):
    pattern = re.compile(pattern_string)
    all_matches = pattern.findall(sample_text)

    return all_matches

def find_matches_iter(sample_text, pattern_string):
    pattern = re.compile(pattern_string)
    find_all_matches = pattern.finditer(sample_text)

    return find_all_matches

def print_result(results):
    if type(results) == re.Match:
        print(results)
    else:
        for result in results:
            print(result)





