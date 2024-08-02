def func(a,b,c):
    D=(b*b)-(4*a*c)
    print('\n',f'D:={D}','\n')
    match D:
        case _ if D>0:
            x= str([((0-b)+D**0.5)/2*a,((0-b)-D**0.5)/2*a ])
        case _ if D==0:
            x=str(((0-b)/2*a))
        case _ if D<0:
            x='решений нет'
    return x

print('\n'*3,'Решение квадратного уравнения ax\u00B2+bx+c=0','\n'*2)

a=float(input('Введите a='))
b=float(input('Введите b='))
c=float(input('Введите c='))

result=func(a,b,c)
print('\n'*2,f'Результат: {result}')
