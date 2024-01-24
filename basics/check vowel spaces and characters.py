string = input("enter a string: ")

count = 0;  
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
   
vowels = 0
for i in string:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1

space_count = 0

for i in range(0, len(string)):
        if string[i] == " ":
            space_count += 1

print("Total number of characters in this string: " ,count)  
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Spaces in this String = ",space_count)