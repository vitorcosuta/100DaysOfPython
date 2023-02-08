from os import name, system
from art import logo

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def add_bidder(bidder_name):
    bidder = {}
    bidder["name"] = bidder_name
    bidder["bid"] = bid_value
    bidders.append(bidder)

def determine_winner(bidders):
    highest_bid = bidders[0]["bid"]
    winner = {
        "name":bidders[0]["name"],
        "bid":highest_bid,
    }
    
    for bidder in bidders:
        value_of_bid = bidder["bid"]
        if value_of_bid > highest_bid:
            highest_bid = value_of_bid
            winner["name"] = bidder["name"]
            winner["bid"] = highest_bid

    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")

end_of_program = False

print(logo)
print("Welcome to the secret auction program.\n")

# Creating empty list to store the bidder's data
bidders = []

while not end_of_program:
    bidder_name = input("What's your name? ")
    bid_value = input("What's your bid? $ ")

    add_bidder(bidder_name)

    continue_to_new_bidder = input("\nAre there any other bidders? \"Yes\" or \"no\" ? ").lower()

    if continue_to_new_bidder == 'no':
        end_of_program = True
        clear()
        determine_winner(bidders)
    if continue_to_new_bidder == 'yes':
        clear()
    