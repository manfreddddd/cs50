
def bank():
    greet=input("Greeting: ")
    if greet == "hello".lower():
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")
bank()