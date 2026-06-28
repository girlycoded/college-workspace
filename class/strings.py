# name: joosan
# desc: practice some common string methods

name = "Sammy Jones"

print(name.upper(), name.lower(), name.title(), len(name))

# str_var.isalpha() - returns True if all characters in the string are alphabetic
print(name.isalpha())

#str_var.trim() - returns a copy of the string with leading and trailing whitespace removed
name_with_spaces = "   Sammy Jones   "
print(name_with_spaces.strip())

weird_string = ",,,,,rrrrrrrrtttttttgggggggg.......rbananana......rrr"
print(weird_string)
print(weird_string.strip("r,.r"))

# str_var.find(substring) - returns the index of the first occurrence of substring in str_var, or -1 if not found

preamble = "We the People of the United States"

index = preamble.find("People")
print(preamble[index:])

print(preamble.lower().find("people"))
print(preamble.find("the", 4, 15))

# str_var.replace(old, new) - returns a copy of the string with all occurrences of old replaced by new
str1 = "I like cats. Cats are great pets."
str2 = str1.replace("cats", "dogs")
print(str1, "\n", str2)

