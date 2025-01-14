import os
print("*****Welcome to theSilent Auction Program*****")


def find_winner(bidder_details):  # (wilfred 10000, ram 34000, shyam 55555)
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"Here is the details of all the bidders; \n{bidder_details}")
    print(f"The Winner is {winner} with a bid price of {highest_bid}")


bidder_data = {}
end_of_bidding = False
while not end_of_bidding:
    name = input("What is you name: ")
    price = int(input("What is your Bid: "))
    bidder_data[name] = price
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        end_of_bidding = True
        find_winner(bidder_data)
    elif more_bidders == 'yes':
        os.system('cls')
