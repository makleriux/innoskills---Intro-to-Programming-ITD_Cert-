string_1 = input("Enter string:")   
if string_1 == string_1[::-1]:
        print(f'"{string_1}" is a palindrome word')
else:
        print(f'"{string_1}" is not a palindrome word')