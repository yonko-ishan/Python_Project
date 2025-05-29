import os
print("*****Silent Auction Program*****")
bids={}

def add_bid(name,bid):
    if name in bids:
        print(f"{name} has already placed a bid of {bids[name]}.")
    else:
        bids[name] = name
        bids[name] = bid
cond=True
while cond:
    name=input("What is your name? ")
    bid=int(input("What is you bid? "))
    yes_no=input("Are there any other biders? Type(yes/no): ")
    add_bid(name,bid)
    if yes_no == 'yes':
        cond=True
        os.system('cls')
    else:
        cond=False
        bid_winner=max(bids, key=bids.get)

print(f"The winner is {bid_winner} with a bid of {bids[bid_winner]}!")