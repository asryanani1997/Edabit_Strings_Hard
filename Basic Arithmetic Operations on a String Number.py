def arithmetic_operation(x):
    num1, operator, num2=x.split(" ")
    num1=int(num1)
    num2=int(num2)
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="//":
        if num2==0:
            return -1
        else:
            return num1//num2
        
print(arithmetic_operation("15 // 0"))
    
    
