num =0
while True:
    try:
        num = int(input("Enter a number: "))
        assert num % 2 != 0
    except:
        print("It is an even number try again")
        continue
    else:
        print("Input is correct.Thank you ")
        break