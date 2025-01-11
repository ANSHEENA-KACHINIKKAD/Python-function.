# Python-function.
Basic python function creation and its working.

## Exercise-1:
   Create a function that takes in three arguments, two of which are optional. The first argument should be a required positional argument, the second argument should be a keyword argument with a default 
   value of 10, and the third argument should be a keyword argument with a default value of None. The function should print the sum of the first two arguments if the third argument is None, and print the 
  product of all three arguments if the third argument is not None.

   code:
  
    def sum_arg(a,b=10,c="none"):
    if c=="none":
        return a+b
    else:
        return a*b*c

    print(sum_arg(2,c=4))
    print(sum_arg(4,b=6))

## Exercise-1:
   Create a function that takes in a list of strings and returns a new list with only the strings that have a length greater than or equal to 5.

   code:
  
    l1=[]
    for i in range(7):
    a= input("enter the list of strings:")
    l1.append(a)
    l2=[]
    def fun_name(l1):
    for i in l1:
        if len(i)>=5:
            l2.append(i)
    return l2

    print(fun_name(l1))



## Exercise-3:
   Python program to evaluate a given mathematical expression using the eval() function. expression = "3 * 5 + 2"

   code:
  
    print("result:",eval("3*5+2"))



## Exercise-4:
   Write a Python program to filter out the prime numbers from a given list of integers using the filter() function.

   code:
  
    l1 = [int(input("Enter the list elements: ")) for _ in range(6)]

    def is_prime(n):
    if n==1:
        return False
    else:
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                return False
        return True
    prime_numbers=filter(is_prime,l1)
    print(list(prime_numbers))



## Exercise-5:
  Write a Python program to convert a list of strings to uppercase using the map() function.

   code:
  
    l1=[input("enter list string element:") for _ in range(5)]
    upper_string=map(lambda x:x.upper(),l1)
    print(list(upper_string))
