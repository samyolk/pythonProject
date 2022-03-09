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
average_absences = sum(days_absent) / len(days_absent)
print("\nAverage absences this year:", average_absences)
print("Person with most days absent:",
      names_list[days_absent.index(max(days_absent))])
while item < len(days_absent):
    if days_absent[item] == 0:
        no_absences.append(names_list[item])
    item += 1
item = 0
no_absences.sort()
print("People with no absences (alphabetical order): ", no_absences)
while item < len(days_absent):
    if days_absent[item] > average_absences:
        above_average.append(names_list[item])
    item += 1
above_average.sort()
print("People above the average number of absence days: ", above_average)
