def factorial_num(n):
    factorial = n
    if n == 0 or n == 1 :
        return 1 
    else:
        
        for i in range (n-1 , 1 , -1):
            factorial = factorial * i
        return factorial
    
num = int(input("Enter a number:"))
result = factorial_num(num)
print(f"The factorial of {num} is : {result}")