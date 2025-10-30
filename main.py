import random
from colorama import Fore, Style
print("------------------- 1 užduotis -------------------")
print()
arr1=[]
for i in range(30):
    arr1.append(random.randint(5,25))
print(arr1)
print()

print("------------------- 2a užduotis -------------------")
print()
count=0
for number in arr1:
    if number > 10:
        count += 1
print(count)
print()

print("------------------- 2b užduotis -------------------")
print()
x=max(arr1)
print(x)
print()

print("------------------- 2c užduotis -------------------")
print()
suma = sum(arr1)
print(suma)
print()

print("------------------- 2d užduotis -------------------")
print()
arr2=[]
for index, number in enumerate(arr1):
    num = number-index
    arr2.append(num)
print(arr2)
print()

print("------------------- 2e užduotis -------------------")
print()
for i in range(10):
    arr1.append(random.randint(5,25))
print(arr1)
print()

print("------------------- 2f užduotis -------------------")
print()
list1 = []
list2 = []
for index, number in enumerate(arr1):
    if index % 2 == 0:
        list1.append(number)
    else:
        list2.append(number)
print(list1)
print(list2)
print()

print("------------------- 2g užduotis -------------------")
print()
for index, number in enumerate(list1):
    if number > 15:
        list1[index] = 0
print(list1)
print()

print("------------------- 2h užduotis -------------------")
print()
indexes_of_low_nums=[]
for index, number in enumerate(list2):
    if number >10:
        indexes_of_low_nums.append(index)
print(indexes_of_low_nums)
print(min(indexes_of_low_nums))
print()

print("------------------- 3 užduotis -------------------")
print()
raides = []
count_A = 0
count_B = 0
count_C = 0
count_D = 0
for i in range(200):
    raides.append(random.choice(['A','B','C','D']))

print(raides)
for i in raides:
    if i == 'A':
        count_A += 1
    if i == 'B':
        count_B += 1
    if i == 'C':
        count_C += 1
    if i == 'D':
        count_D += 1
print(f"{Fore.LIGHTMAGENTA_EX}A kiekis: {count_A}{Style.RESET_ALL}")
print(f"{Fore.BLUE}B kiekis: {count_B}{Style.RESET_ALL}")
print(f"{Fore.RED}C kiekis: {count_C}{Style.RESET_ALL}")
print(f"{Fore.CYAN}D kiekis: {count_D}{Style.RESET_ALL}")

print("------------------- 4 užduotis -------------------")

#git config --global user.name "AdomasSl"

#git config --global user.email "adomas.slusnys@gmail.com"
