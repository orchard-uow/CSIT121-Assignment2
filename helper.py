# Convert string to snake_case
# file sourced from w3resource
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-97.php

from re import sub

# Define a function to convert a string to snake case
def snake_case(s):
    # Replace hyphens with spaces, then apply regular expression substitutions for title case conversion
    # and add an underscore between words, finally convert the result to lowercase
    return '_'.join(
        # find uppercase letter followed by lowercase letter
        # insert space before 
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()