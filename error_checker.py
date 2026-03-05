try:
    num1, num2 = eval(input("enter two numbers, seperated with a coma: "))
    result = num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is a error !!!")
except SyntaxError:
    print("coma is missing. enter numbers seperated by coma like this 1, 2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will excute no matter what.")