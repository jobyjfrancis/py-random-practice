"""str_input = input("Enter a string: ")
print("The string you entered: ", str_input)
print("Here are the characters at even index of this string: ")

for i in range(0, len(str_input), 2):
    print(str_input[i])"""

# Another method using list slicing
str_input = input("Enter a string: ")
print("The string you entered: ", str_input)
print("Here are the characters at even index of this string: ")

str_list = list(str_input)
for i in str_list[0::2]:
    print(i)











