from art import logo
from os import name, system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def encrypt(text, shift):

    encrypted_text = list(text)
    for i in range(len(text)):
        
        position = alphabet.index(text[i])
            
        for k in range(shift):
            if position < 25:
                position += 1
            else:
                position = 0
            
        encrypted_text[i] = alphabet[position]
        
    print(f"Here's the encoded result: {''.join(encrypted_text)}\n")

def decrypt(text, shift):

    decrypted_text = list(text)
    for i in range(len(text)):

        position = alphabet.index(text[i])

        for k in range(shift):
            if position > 0:
                position -= 1
            else:
                position = 25

        decrypted_text[i] = alphabet[position]

    print(f"Here's the decoded result: {''.join(decrypted_text)}\n")

end_of_program = False

while not end_of_program:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    
    elif direction == "decode":
        decrypt(text, shift)

    continue_running = input("Type 'Yes' to run the program again, otherwise type 'No':\n").lower()

    if continue_running == "yes":
        clear()
    elif continue_running == "no":
        print("\nThis program finished running.")
        end_of_program = True

