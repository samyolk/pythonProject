BASECOST = 10
DOLLAR_PER_MIN = 2
minutes = []

driver_name = input("What is your name? ")


def taxi_trip():
    new_trip = "Y"
    while new_trip != "N":
        new_trip = input("Would you like to start a new trip? (Y/N) ").upper()
        if new_trip == "Y":
            minutes.append(int(input("How many minutes did the trip take? ")))
        elif new_trip != "Y" and new_trip != "N":
            print("Please enter Y for yes and N for no")


def end_print_screen():
    if len(minutes) > 0:
        print("\n--------------------")
        print(driver_name)
        print("total time: ", sum(minutes), "minutes")
        print("average time: ", sum(minutes) / len(minutes), "minutes")
        print("total income: $", sum(minutes) * DOLLAR_PER_MIN + BASECOST)
        print("--------------------")
    else:
        print("\n--------------------")
        print(driver_name)
        print("total time: 0 minutes")
        print("average time: 0 minutes")
        print("total income: $0")
        print("--------------------")


taxi_trip()
end_print_screen()
