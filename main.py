def num_translate(n):
    num={'one' : 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять', 
    'six' : 'шесть', 'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}
    if n in num:
        return print(num[n])
    else:
        n = input('Ошибка ввода, попробуйте ещё раз: ')
        num_translate(n.casefold())

n = input('введите число на английском (1-10): ')
num_translate(n.casefold())