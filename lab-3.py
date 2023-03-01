
#---------------------------------
# price = float(input())
# for i in range(1,11):
#     i = i*price
#     print(i)

#---------------------------------
# sum = 0
# sansum = 0
# san = int(input('>> '))
# while san != 0:
#     sum += san
#     sansum += 1
#     san = int(input('>> '))
# print(sum, sansum)

#---------------------------------
# import random
# a=0
# b=40
# random_integer = random.randint(a, b) 
# print("The random integer is :", random_integer)

#---------------------------------
# from random import randint

# m=int(input("Введите вол-во строк "))
# n=int(input("Введите вол-во стоблцов "))

# print("Элементы массива:")
# a = [[randint(1,10) for j in range(n)] for i in range(m)]
# for i in range(m):
#   print(a[i],max(a[i]))
# for i in range(n):
#   x=[x[i] for x in a]
# print(min(x), end=" ")

#---------------------------------
# seq = list('BEKZHIGIT')
# for i, val in enumerate(seq, start=1):
#   print(f'№ {i}: {val}')

#---------------------------------
# a=int(input())
# b=int(input())
# for i in range(a-1,b):
#   i=i+1
#   print(i)

#---------------------------------
# a=int(input())
# b=int(input())
# if a<b:
#   for i in range(a, b+1):
#     print(i)
# else:
#   for i in range(a, b-1, -1):
#     print(i)

#---------------------------------
# a=int(input())
# b=int(input())
# for i in range(a-(a+1)%2, b-b%2, -2):
#   print(i, end=" ")

#---------------------------------
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# for i in range(n - 1):
#     sum -= int(input())
# print(sum)
#--------------------------------