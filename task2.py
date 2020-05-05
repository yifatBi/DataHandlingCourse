# 1. Print elem in l
l = ['hello', 'list', 'item']
elem = 'hello'
print(elem in l)
# 2. Print nth word
line = input('2.Enter your line: ')
i = int(input('2.Enter nth word: '))
print(line.split()[i - 1])
# 3. list of numbers
l = [3, 4, 2, 2, 0, -4]
l.sort()
print(l[0])
# 4. Sum of odd numbers between 2 positive numbers
n = int(input('4.Non negative n: '))
m = int(input('4.Non negative m: '))
max_number = max(n, m)
min_number = min(n, m)
min_odd = min_number + 2 if min_number % 2 != 0 else min_number + 1
sum_number = 0

# 4.i- for loop
for x in range(min_odd, max_number, 2):
    sum_number += x
print(sum_number)
# 4.ii - while
x = min_odd
sum_number = 0
while x < max_number:
    sum_number += x
    x += 2
print(sum_number)

# challenge
input_value = int(input('Add a number: '))
l = []
while input_value > -1:
    l.append(input_value)
    input_value = int(input('Add a number: '))
if len(l) == 0:
    print(l)
elif input_value % 2 == 0:
    print(l[::2])
else:
    l.sort()
    print(l[1::2])



