from art import logo

print(logo)
print("Welcome to the secret auction program")

additional_bidders = True
bidders_lst = []

while additional_bidders:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidder_dic = {"name": name, "bid": bid}
    bidders_lst.append(bidder_dic)
    if others == "no":
        additional_bidders = False
    elif others == "yes":
        print("\n" * 100)


def find_highest_bid(bid_lst):
    bids = [x['bid'] for x in bid_lst]
    highest_bid = max(bids)
    highest_pos = bids.index(highest_bid)
    highest_bidder = bidders_lst[highest_pos]
    return highest_bidder


highest_bidder = find_highest_bid(bidders_lst)

print("The highest bidder was {} with an amount of ${}".format(
    highest_bidder['name'], highest_bidder['bid']))
