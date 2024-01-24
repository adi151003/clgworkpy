list = []
number = 5
for n in range(number):
    numbers = int(input('Enter numbers '))
    list.append(numbers)
    
print("Maximum element in the list is :", max(list))