# 1.Print email
email = 'ifatbiezuner@mail.tau.ac.il'
print(email)
# 2. Print value and length
inputValue = input('2: ')
print(inputValue)
print(len(inputValue))
# 3. Three first chars in lowercase
inputValue = input('3: ')
print(inputValue[:3].lower())
# 4. Print every chars backwords
inputValue = input('4: ')
print(inputValue[1::2][::-1])
# 5. Print input length minus spaces
inputValue = input('5: ')
print(len(inputValue.replace(' ', '')))
# 6. int input print n times
i = int(input('6: '))
print('I will submit my assignments on time\n'*i)
# 7. some logic
text = input('7:text: ')
start = int(input('7:start: '))
end = int(input('7:end: '))
copy = int(input('7:copy: '))
print(*[text[start:end]]*copy)
# Challenge
text = input('text')
start = int(input('start'))
end = int(input('end'))
copy = int(input('copy'))
if start < 0 or end < start or copy < 1 or end > len(text):
    print('Error: illegal input!')
else:
    print(*[text[start:end]]*copy)
