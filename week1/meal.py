def main():
    time=input("What time is it? ")
    convert(time)

def convert(time):
    h,m = time.split(":")
    new_time=int(h) + int(m)/60

    if new_time >= 7.0 and new_time <= 8.0:
        print("breakfast time")
    elif new_time >= 12.0 and new_time <= 13.0:
        print("lunch time")
    elif new_time >= 18.0 and new_time <= 19.0:
        print("dinner time")
    else:
        print("")


if __name__ == "__main__":
    main()