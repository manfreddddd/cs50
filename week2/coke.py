# ask for user input
# check if user input 50 cents?
# output the change


    
def coke():
    accepted_coins = [25, 10, 5]
    total = int(50)
    while True:
        print(f"Amount Due: {total}")
        insert = int(input("Insert Coin: "))
        if insert in accepted_coins:
            total -= insert
            if total < 0:
                print(f"Change Owed: {total}") 
                break
            if total == 0:
                print("Change Owed: 0")
                break

coke()

            








