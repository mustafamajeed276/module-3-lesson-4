try:
    number = int(input("enter a number"))
    print("the number enter is ", number)
except ValueError as ex:
    print("exception : ", ex)