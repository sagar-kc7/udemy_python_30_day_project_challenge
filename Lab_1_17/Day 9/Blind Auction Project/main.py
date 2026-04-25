from art import logo

print(logo)
total_bid ={}

again = "yes"
while again == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    total_bid[name] = bid
    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if again == "yes":
        print("\n" * 20)
print(total_bid)

winner = ""
highest_bid = 0
for key in total_bid:
    if total_bid[key] >= highest_bid:
        highest_bid = total_bid[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")
