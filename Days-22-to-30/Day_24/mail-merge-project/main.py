#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open('Input/Names/invited_names.txt', mode='r') as name_list:
    name_lines = name_list.readlines()
    names = []

    # We must first remove "\n" in the file lines in order to obtain the proper name strings.
    for line in name_lines:
        name = line.strip('\n')
        names.append(name)

with open('Input/Letters/starting_letter.txt', mode='r') as starting_letter:

    # The read() method returns the specified amount of content in the file (or everything if no parameter)
    # as a string (in text mode) or bytes object (in binary mode)
    original_letter = starting_letter.read()

for name in names:

    edited_letter = original_letter.replace(PLACEHOLDER, name)
    file_path = f"Output/ReadyToSend/letter_for_{name}.txt"

    with open(file_path, mode='w') as final_letter:

        final_letter.write(edited_letter)
