# Regex


# problem:

Check the email address was entered by user,
that is in this general form:

**expression@string.string**
# solution:
## First

import **regex**:

    import re

Actually,regex or regular expression is a sequence of characters that define a **search pattern**.
usually such pattern used by **string searching** algorithm for find and replace operations on strings or for input validation.
## Second

Lets define used characters:

    s=re.search(r'[^\W]+\@\w+[^\d]\.\w[^\d]+$',m)

 - [^\W] :     all words and digits
 - \w :  all words
 - [^\d] : all except digits = not digits (\d : means digits)
 - \$ : end of the string
 - \+ : at least one number

## Third

if it can  not find desired string ,output will be **none**
and if it can ,output will be number of the character **started** and **ended** desired string. 
 like this:

    s.span()
    >> (0, 20) 
    
