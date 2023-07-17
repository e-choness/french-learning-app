# python-regex-full

Extensive practices of python regex syntax and use cases.

- [x] re module
- [x] Methods to search for matches
- [x] Methods on a match object

- match(): Determin if the RE matches at the beginning of the string.
- search(): Scan through a string, looking for any location where this RE matches.
- findall(): Find all substrings where the RE matches, and returns them as a list.
- finditer(): Find all substrings where the RE matches, and returns them as an iterator.

- [x] Meta characters

Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with ) if we actually want to search for the char.

- . Any character (except newline character) "he..o"
- ^ Starts with "^hello"
- \$ Ends with "world\$"
- \* Zero or more occurrences "aix*"
- \+ One or more occurrences "aix+"
- { } Exactly the specified number of occurrences "al{2}"
- \[] A set of characters "[a-m]"
- \ Signals a special sequence (can also be used to escape special characters) "\d"
- | Either or "falls|stays"
- ( ) Capture and group

- [x] More special sequences

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

- \d :Matches any decimal digit; this is equivalent to the class [0-9].
- \D : Matches any non-digit character; this is equivalent to the class [^0-9].
- \s : Matches any whitespace character;
- \S : Matches any non-whitespace character;
- \w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
- \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
- \b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
- \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
- \A Returns a match if the specified characters are at the beginning of the string "\AThe"
- \Z Returns a match if the specified characters are at the end of the string "Spain\Z"
- 
- [ ] Sets
- [ ] Quantifier
- [ ] Conditions
- [ ] Grouping
- [ ] Modification
- [ ] Compilation flags
