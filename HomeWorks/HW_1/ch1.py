# Вариант 1:
def summ(a, b, c, d):
    return (a + b + c + d)


a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
d = int(input('Enter 4th number: '))

print(f'Sum of {a},{b},{c} and {d} is {summ(a, b, c, d)}')

# Вариант 2:

result: int = 0
for i in range(4):
    result += int(input(f'Enter {i + 1} number: '))
print(f'Sum of the numbers: {result}')
