def highest(record):
    highestBid = 0
    winner = ""
    for i in record:
        amount = record[i]
        if amount > highestBid:
            highestBid = amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highestBid}")
 
bids= {}

finish = False

while not finish:
    name = input("Name: ")
    price =int(input("bid: "))

    bids[name] = price
    yn = input("Are there other bidders (y/n): ").lower()
    
    if yn == "n":
        finish = True
        highest(bids)







