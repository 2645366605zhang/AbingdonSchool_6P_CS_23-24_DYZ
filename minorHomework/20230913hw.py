name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']
num_list = []
num_list_index = 0
largest = ""
smallest = ""
total = 0

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)

print(f"The third name is: {name_list[2]}")
print(f"The last seven names are: {name_list[len(name_list) - 7]}, {name_list[len(name_list) - 6]}, {name_list[len(name_list) - 5]}, {name_list[len(name_list) - 4]}, {name_list[len(name_list) - 3]}, {name_list[len(name_list) - 2]}, {name_list[len(name_list) - 1]}")

for i in range(5):
    num_list.append(int(input("Please enter an integer: ")))

for num in num_list:
    if num_list_index == 0:
        last_num = num
    elif num_list_index == 1:
        if num > last_num:
            largest = num
            smallest = last_num
        elif num < last_num:
            smallest = num
            largest = last_num
        last_num = num
    else:
        if num > largest:
            largest = num
            if num < smallest:
                smallest = last_num
        last_num = num
    num_list_index += 1
    total += num

mean = total / 5

print(f"Largest: {largest}\nSmallest: {smallest}\nMean: {mean}")


