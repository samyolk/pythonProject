import time
children = []
leave = False
PERHOURCOST = 12


def dropoff():
    name = input("What is the child's name? ")
    children.append(name)


def pickup():
    name = input("what is the child's name? ")
    if name in children:
        print("Ok, here is your child")
        children.remove(name)
        time.sleep(1.5)
    else:
        print("Sorry, but we don't have anyone with that name ")
        time.sleep(1.5)


def calcost():
    stop = False
    hours = int(input("How many hours do you intend to leave "
                      "your child at this daycare? "))
    while stop is False:
        morechildans = input("Do you have any other children you want to"
                             " leave at this daycare? (Y/N) ").upper()
        if morechildans == "Y":
            hours += int(input("How many hours do you intend to leave your"
                               " child at this daycare?"))
        elif morechildans == "N":
            stop = True
        else:
            print("Please enter a valid answer (Y for Yes and N for No)")

    print("That will cost $", PERHOURCOST * hours)
    time.sleep(1.5)


def printroll():
    print(children)
    time.sleep(1.5)


while leave is False:
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("---------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()
    if choice == 1:
        dropoff()
    elif choice == 2:
        pickup()
    elif choice == 3:
        calcost()
    elif choice == 4:
        printroll()
    else:
        print("Goodbye")
        leave = True
