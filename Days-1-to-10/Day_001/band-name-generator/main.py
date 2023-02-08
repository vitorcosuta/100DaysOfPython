#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

print('Hello and welcome to Band Name Generator!\n')

user_city_name = input("What's the name of the city you grew up in? ")
user_pet_name = input("What's your pet's name? ")

print("\nCan I suggest a name for your band? It could probably be: "+ user_city_name + " " + user_pet_name)