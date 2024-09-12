try:
    num1, num2 = eval(input("enter two numbers seperated with a ',' like this, 1, 2:"))
    result = num1 / num2
    print("result is ", result)
except ZeroDivisionError:
    print("you can't divide by zero!!")
except SyntaxError:
    print("seperate them with a ',' like this, 1, 2!!")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will run no matter what")