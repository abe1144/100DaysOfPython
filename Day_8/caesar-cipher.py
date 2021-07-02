from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
print(logo)


# function that encrypts or decrypts
def caesar(text, shift, direction):
    transformed_text = ""
    if direction == "encode":
        for char in text:
            if char in alphabet:
                char_pos = alphabet.index(char)
                encrypt_char = alphabet[(char_pos + shift) % len(alphabet)]
                transformed_text = transformed_text + encrypt_char
            else:
                transformed_text = transformed_text + char
        print("The encoded text is {}".format(transformed_text))
    elif direction == "decode":
        for char in text:
            if char in alphabet:
                char_pos = alphabet.index(char)
                encrypt_char = alphabet[char_pos - shift]
                transformed_text = transformed_text + encrypt_char
            else:
                transformed_text = transformed_text + char
        print("The decoded text is {}".format(transformed_text))


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)
    again = input("Type 'yes' if you want to go again, Otherwise type 'no':\n")
    if again == "no":
        should_continue = False
