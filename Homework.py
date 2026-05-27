user_input = input("Enter a character: ")

is_lowercase_alphabet = (user_input >= 'a' and user_input <= 'z')

is_uppercase_alphabet = (user_input >= 'A' and user_input <= 'Z')

is_alphabet = (is_lowercase_alphabet or is_uppercase_alphabet)

if is_alphabet:
    print("It is an alphabet.")
else: 
    print("It is not an alphabet.") 
