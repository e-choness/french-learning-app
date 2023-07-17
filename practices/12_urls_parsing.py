import practices.re_module as rm

# This is an example of urls parsing using regex.
urls = """
http://python-engineer.com
https://www.google.com
http://e-choness.github.io/portfolio-site
"""
pattern_string = r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)'

matches_iter = rm.find_matches_iter(urls, pattern_string)
rm.print_result(matches_iter)