auction_item = input("What is the auction for? ")
reserve_price = float(input("What is the reserve price? $"))


def auction():
    highest_bid = 0
    current_bid = 0
    while current_bid != -1:
        print("\nThe current highest bid for", auction_item, "is $",
              highest_bid)
        current_bid = float(input("What is your bid? $"))
        if current_bid > highest_bid:
            highest_bid = current_bid
    if highest_bid >= reserve_price:
        print(auction_item, "was sold at a price of $", highest_bid)
    else:
        print("The highest bid for", auction_item, "did not meet the reserve"
                                                   " price and was not sold.")


auction()
