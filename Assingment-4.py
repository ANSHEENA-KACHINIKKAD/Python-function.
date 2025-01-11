
# Exercise-1:
# def sum_arg(a,b=10,c="none"):
#     if c=="none":
#         return a+b
#     else:
#         return a*b*c
#
# print(sum_arg(2,c=4))
# print(sum_arg(4,b=6))


# Exercise-2:
# l1=[]
# for i in range(7):
#     a= input("enter the list of strings:")
#     l1.append(a)
# l2=[]
# def fun_name(l1):
#     for i in l1:
#         if len(i)>=5:
#             l2.append(i)
#     return l2
#
# print(fun_name(l1))

#Exercise-3:
# print("result:",eval("3*5+2"))

# Exercise-4:
# l1 = [int(input("Enter the list elements: ")) for _ in range(6)]
#
# def is_prime(n):
#     if n==1:
#         return False
#     else:
#         for j in range(2,int(n**0.5)+1):
#             if n%j==0:
#                 return False
#         return True
# prime_numbers=filter(is_prime,l1)
# print(list(prime_numbers))


# Exercise-5
l1=[input("enter list string element:") for _ in range(5)]
upper_string=map(lambda x:x.upper(),l1)
print(list(upper_string))