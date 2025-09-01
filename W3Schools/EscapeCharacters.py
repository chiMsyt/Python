# Escape Characters

# To insert characters that are illegal in a string, use an escape character
# escape character -> \ , followed by the character you want to insert

# an example of an illegal character is a double quotes inside a string that is surrounded by double quotes
txt = "We are the so-called "Vikings" from the north." # type: ignore
# to fix this, use \
txt = "We are the so-called \"Vikings\" from the north."

# Other escape characters used in Python
# \' Single Quote
# \\ Backslash
# \n New Line
# \r Carriage Return
# \t Tab
# \b Backspace
# \f Form Feed
# \ooo Octal Value
# \xhh Hex Value