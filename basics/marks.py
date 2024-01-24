marks=[31,45,65,23,90,87]
print("The list of marks is: ",marks)
n=int(input("Enter marks to append: "))
marks.append(n)
marks
min(marks)
print("The minimum marks among list is",min(marks))
marks.remove(min(marks))
print(marks)
print("The max marks is",max(marks))
marks[4]=49
print(marks) 