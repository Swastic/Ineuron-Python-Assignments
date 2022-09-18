#!/usr/bin/env python
# coding: utf-8

# Q1: The re.compile() function returns Regex object.

# Q2: Raw strings are used so that backlashes do not have to be escaped.

# Q3: The search() method returns the Match objects.

# Q4: The group() method returns strings of the matched text.

# Q5: Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parantheses.

# Q6: Periods and parantheses can be escaped with a backslash: \.,\(, and \).

# Q7: If regex has no groups a list of strings is returned. If the regex has groups, a list of tuples of strings is returned. 

# Q8: The | character signifies matching "either, or" between two groups.

# Q9: Character not mentioned.

# Q10: + matches one or more. * matches 0 or more.

# Q11: The {4} matches exactly three instances of the preceding group. The {4,5} matches between four and five instances.

# Q12: The \d,\w and \s shorthand classes matches a single digit, word, or space character, respectively.

# Q13: The \D,\W and \S shorthand classes matches a single character that is not a digit, a word, or a space character, respectively.

# Q14: The .* performs a greedymatch, and .*? performs a nongreedy match.

# Q15: [0-9a-z] or [a-z0-9]

# Q16: By passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.

# Q17: The . character normally matches any character except the newline character.If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.

# Q18: 'X drummers,X pipers, five rings, X hens'

# Q19: The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().

# Q20: e.compile(r'^\d{1,3}(,{3})*$') will create this regex, but other regex strings can produce a similar regular expression.

# Q21: re.compile(r'[A-Z][a-z]*\sWatanabe')

# Q22: re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\ s(apples|cats|baseballs)\.', re.IGNORECASE)

# In[ ]:




