def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False

    if not plate[:2].isalpha():
        return False

    if not plate.isalnum():
        return False

    for i in range(len(plate)):
        if plate[i].isdigit():
            if not plate[i:0].isdigit():
                return False
            if plate[i] == "0":
                return False
            break
    return True
    
                                   
                     

main()