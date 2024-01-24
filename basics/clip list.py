class ClipList:
    def __init__(self):
        self.max=int(input("Enter max element : "))
        self.min=int(input("Enter min element : "))

    def list_elements(self):
        lst = []
        n = int(input("Enter number of elements : "))
        for i in range(n):
            ele = int(input("Enter element "+str(i+1)+" : "))
            if ele>self.max:
                print("Do you want to change the max element in the list")
                a =int(input("Enter 1 for yes and 2 for no : "))
                if a ==1:
                    print("Now the max element is ",ele)
                    self.max=ele
                    lst.append(ele)
                elif a==2:
                    print("start the list again")
                    s.list_elements()
                else:
                    print("Wong input")
                    s.list_elements()
            elif ele<self.min:
                print("Do you want to change the min element in the list")
                a=int(input("Enter 1 for yes and 2 for no : "))
                if a==1:
                    print("Now the min element is ",ele)
                    self.min=ele
                    lst.append(ele)
                elif a==2:
                    print("start the list again")
                    s.list_elements()
                else:
                    print("Wong input")
                    s.list_elements()

            else:
                lst.append(ele)
        print(lst)
        print(self.max)
        print(self.min)

s= ClipList()
s.list_elements()