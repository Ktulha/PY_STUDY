list_1 = [x + 5 for x in range(10)]
print(list_1)
list_2 = list_1[::2]
print(list_2)
d = 1
for x in list_2:
    d *= x
print(d)
t = 0
for x in list_2:
    t += x
print(t)
list_3 = list_2 + [t, d]
print(list_3)
list_3.sort(reverse=True)
print(list_3)
list_4 = [str(x) for x in list_3]
print(list_4)
text = "=".join(list_4)
print(text)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]
b = [x for x in a if x < 5]
print(b)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]
c = [x for x in b if x in a]
c.sort()
print(c)
s = 'kafka python course stack flow dict list python stack course star product star product analytics flow star kafka stack flow ython list set ist fit predict dict list python ourse ython ourse star product ist fit predict analytics kafka stack flow product ist fit predict analytics star flow dict flow list python course stack flow dict list python stack course'
ls1 = s.split()
print(ls1)
words = dict()
for i in ls1:
    if words.get(i):
        words[i] += 1
    else:
        words[i] = 1
print(words)
print(f'{max(words, key=words.get)} {max(words.values())}')

names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat', 'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']

occupations = ['smm', 'developer', 'analyst', 'president', 'analyst', 'ceo', 'customer development', 'founder',
               'developer', 'ml engineer', 'product manager', 'cmo']
workers = dict(zip(names, occupations))
print(workers['maria'])

dict1 ={'1': 10, '2': 20, '3901': 11, '384': 13, '8489': 1, '48': 10}

dict2 = {'3': 30, '4': 40, '93': 12, '91': 41, '95': 1, '841': 11, '584': 11}

dict3 = {'5': 50, '6': 60, '9': 90, '3': 13, '7': 11}
dict4=dict(dict1,**dict2)
dict4=dict(dict4,**dict3)
dd=dict()
for key,val in dict4.items():
    if dd.get(val):
        dd[val]+=1
    else:
        dd[val]=1

print(dict4)
print(f'{len(dict4)},{max(dd, key=dd.get)},{max(dd.values())} ')
print(dd)
given_string = 'Python Star Course for beginners and experts for data science and analytics without sql with code'
txt=given_string.replace(" ",'')
dict5=dict()
for i in txt:
    if dict5.get(i):
        dict5[i]+=1
    else:
        dict5[i]=1
print(dict5)
dict6=list(sorted(dict5.items(),key=lambda x:x[1]))
print(dict6)
m=[]
for i in range(8):
    m.append(dict6[i][0])
print(''.join(m))
