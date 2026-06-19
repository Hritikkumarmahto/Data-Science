# strip()

str1="  Hritik  "
#str1.strip()   # use to remove space and unwanted error s
print(str1.strip())   

# lstrip - use to remove from left
# rstrip- use to remove from right
# strip - will remove from both the end 

# we can also use this to check if the string is ending or strrting with any special word

# endswith()

email="Hritik#@gamil.com"
print(email.endswith(".com"))    # wll return true or false 

# start with

name="Hritik"
print(name.startswith("H"))


# find()

name="hritik kumar mahto"

finds=name.find("a")  # returns the first index of occurence of the element
print(finds)

# index

i=name.index("h",1)   # skip first chek for next

print(i)




# similarly 


"""
+----------------+---------------------------------------------------------------+
| Method         | Description                                                   |
+----------------+---------------------------------------------------------------+
| capitalize()   | Converts the first character to upper case                   |
+----------------+---------------------------------------------------------------+
| casefold()     | Converts string into lower case                              |
+----------------+---------------------------------------------------------------+
| center()       | Returns a centered string                                    |
+----------------+---------------------------------------------------------------+
| count()        | Returns the number of times a specified value occurs         |
+----------------+---------------------------------------------------------------+
| encode()       | Returns an encoded version of the string                     |
+----------------+---------------------------------------------------------------+
| endswith()     | Returns True if the string ends with the specified value     |
+----------------+---------------------------------------------------------------+
| expandtabs()   | Sets the tab size of the string                              |
+----------------+---------------------------------------------------------------+
| find()         | Searches the string and returns the position found           |
+----------------+---------------------------------------------------------------+
| format()       | Formats specified values in a string                         |
+----------------+---------------------------------------------------------------+
| format_map()   | Formats values from a dictionary in a string                 |
+----------------+---------------------------------------------------------------+
| index()        | Searches the string and returns the position found           |
+----------------+---------------------------------------------------------------+
| isalnum()      | Returns True if all characters are alphanumeric             |
+----------------+---------------------------------------------------------------+
| isalpha()      | Returns True if all characters are alphabetic               |
+----------------+---------------------------------------------------------------+
| isascii()      | Returns True if all characters are ASCII                     |
+----------------+---------------------------------------------------------------+
| isdecimal()    | Returns True if all characters are decimals                  |
+----------------+---------------------------------------------------------------+
| isdigit()      | Returns True if all characters are digits                    |
+----------------+---------------------------------------------------------------+
| isidentifier() | Returns True if the string is a valid identifier             |
+----------------+---------------------------------------------------------------+
| islower()      | Returns True if all characters are lower case                |
+----------------+---------------------------------------------------------------+
| isnumeric()    | Returns True if all characters are numeric                   |
+----------------+---------------------------------------------------------------+
| isprintable()  | Returns True if all characters are printable                 |
+----------------+---------------------------------------------------------------+
| isspace()      | Returns True if all characters are whitespaces               |
+----------------+---------------------------------------------------------------+
| istitle()      | Returns True if the string follows title case rules          |
+----------------+---------------------------------------------------------------+
| isupper()      | Returns True if all characters are upper case                |
+----------------+---------------------------------------------------------------+
| join()         | Joins iterable elements into a string                        |
+----------------+---------------------------------------------------------------+
| ljust()        | Returns a left-justified version of the string               |
+----------------+---------------------------------------------------------------+
| lower()        | Converts a string into lower case                            |
+----------------+---------------------------------------------------------------+
| lstrip()       | Removes leading whitespace                                   |
+----------------+---------------------------------------------------------------+
| maketrans()    | Returns a translation table                                  |
+----------------+---------------------------------------------------------------+
| partition()    | Splits the string into three parts                           |
+----------------+---------------------------------------------------------------+
| replace()      | Replaces a value with another value                          |
+----------------+---------------------------------------------------------------+
| rfind()        | Returns the last position of a specified value               |
+----------------+---------------------------------------------------------------+
| rindex()       | Returns the last position of a specified value               |
+----------------+---------------------------------------------------------------+
| rjust()        | Returns a right-justified version of the string              |
+----------------+---------------------------------------------------------------+
| rpartition()   | Splits the string into three parts from the right            |
+----------------+---------------------------------------------------------------+
| rsplit()       | Splits the string from the right and returns a list          |
+----------------+---------------------------------------------------------------+
| rstrip()       | Removes trailing whitespace                                  |
+----------------+---------------------------------------------------------------+
| split()        | Splits the string and returns a list                         |
+----------------+---------------------------------------------------------------+
| splitlines()   | Splits the string at line breaks                             |
+----------------+---------------------------------------------------------------+
| startswith()   | Returns True if string starts with specified value           |
+----------------+---------------------------------------------------------------+
| strip()        | Removes leading and trailing whitespace                      |
+----------------+---------------------------------------------------------------+
| swapcase()     | Swaps lower case and upper case characters                   |
+----------------+---------------------------------------------------------------+
| title()        | Converts first character of each word to upper case          |
+----------------+---------------------------------------------------------------+
| translate()    | Returns a translated string                                  |
+----------------+---------------------------------------------------------------+
| upper()        | Converts a string into upper case                            |
+----------------+---------------------------------------------------------------+
| zfill()        | Pads the string with zeros at the beginning                  |
+----------------+---------------------------------------------------------------+
"""
vars="h"
print(vars)