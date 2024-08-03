import time
from random import shuffle, randint


# ######Украшательства#######

def stl(text: str, **kwargs):
    for key, val in kwargs.items():
        text = colorize(text, '' + str(val), key)
    return text


def colorize(text: str, rgb: str, tp='bg'):
    color = {'Red': '155;30;10',
             'Blue': '20;40;140',
             'White': '255;255;255',
             'Black': '0;0;0',
             'Green': '30;100;10'}
    try:
        col = color[rgb.capitalize()]
    except:
        col = rgb

    return {'bg': '\x1b[48;2;{0}m{1}\x1b[49m'.format(col, text),
            'fg': '\x1b[38;2;{0}m{1}\x1b[39m'.format(col, text),
            'bold': '\x1b[1m' + text + '\x1b[0m',
            'italic': '\x1b[3m' + text + '\x1b[0m',
            'underline': '\x1b[4m' + text + '\x1b[0m',
            'revert': '\x1b[7m' + text + '\x1b[0m',
            'strike': '\x1b[9m' + text + '\x1b[0m'}[tp]


# ######## Викторина #########
def quiz_data():
    a, b, c = (randint(1, 10) for _ in range(3))

    qry = [('Какая самая популярная кодировка? : ', 'utf-8'),
           ('Какая версия языка сейчас актуальна? : ', 'Python 3'),
           ('Сколько значений есть у bool? : ', '2'),
           ('Чему равно выражение: {0}+{1}*{2}='.format(a, b, c), str(a + b * c)),
           ('Чему равно двоичное число {0} в десятеричном формате? : '.format(format(c, 'b')), str(c)),
           ('Чему равно "Саша"+"Маша"? : ', "Саша" + "Маша"),
           ('Что выдаст выражение "Саша"-"Маша"? : ', "ошибку"),
           ('Чему равно выражение "False|True"? : ', False | True),
           ('Каким оператором можно прервать выполнение цикла? : ', 'break'),
           ('Каким оператором обозначается выражение "иначе если" ? : ', 'elif')]

    shuffle(qry)
    return qry


def quiz():
    qry = quiz_data()
    t = 0
    cnt = 0
    ctime = time.time()
    for item in qry:
        while t == 0:
            cnt += 1
            answ = str(input(stl(item[0], bold=True, underline=True, fg='white', bg='blue')))
            tmp = answ.replace(' ', '').replace('-', '').lower()
            result = tmp == str(item[1]).replace(' ', '').replace('-', '').lower()
            if result:
                print(stl('Ответ "{0}" верен! \n (точный ответ: "{1}")'
                          .format(answ, item[1]), bg='green', fg='white'))
                break
            else:
                print(stl('"{}" - неверный ответ!\n'.format(answ), bg='red', fg='white', bold=True))
    print('\n' * 3)
    print(stl('На ответы затрачено {0} сек.\n'.format(int(time.time() - ctime)), revert=True))
    print(stl('Результат: \n {0} ответов за {1} попыток\n'
              .format(len(qry), cnt), bg='green', fg='white', bold=True))
    res = int(len(qry) / cnt * 100)
    txt = stl('Эффективность {0}% \n'.format(res), bold=True)
    match res:
        case _ if res > 95:
            txt = stl(txt, bg='Green', fg='white')
        case _ if res < 55:
            txt = stl(txt, bg='Red', fg='white')
        case _:
            txt = stl(txt, bg='255;255;10', fg='black')

    print(txt)


quiz()
