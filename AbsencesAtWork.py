names_list = []
days_absent = []
no_absences = []
above_average = []
item = 0
name = ""
highest_absent = 0


def int_checker(question):
    error = "Please enter a number"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


while name != "$":
    name = input("\nEnter name: ")
    if name != "$":
        days_absent.append(int_checker("Enter amount of days absent: "))
        names_list.append(name)

print("\nAverage absences this year:", sum(days_absent) / len(days_absent))
print("Person with most days absent:",
      names_list[days_absent.index(max(days_absent))])
while item < len(days_absent):
    if days_absent[item] == 0:
        no_absences.append(names_list[item])
    print(item)
    item += 1
no_absences.sort()
print(no_absences)

