one={1:'one',       2:'two',        3:'three',      4:'four',     5:'five',
     6:'six',       7:'seven',      8:'eight',      9:'nine',    10:'ten',
    11:'eleven',   12:'twelve',    13:'thirteen',  14:'fourteen',15:'fifteen',
    16:'sixteen',  17:'seventeen', 18:'eighteen',  19:'nineteen', 0:''}
two={2:'twenty',3:'thirty', 4:'forty', 5:'fifty',
     6:'sixty', 7:'seventy',8:'eighty',9:'ninety',10:''}
#s=int(input('n:'))
def f(s):
    if 0<s<20:
        print(one[s])
    elif 100>s>19:
        print(two[s//10]+' '+one[s%10])
    elif 1000>s>99:
        if -1<(s%100)<20:
            print(one[s//100]+' '+'hundred'+one[s%100])
        else:
            print(one[s//100]+' '+'hundred'+two[s%100//10]+' '+one[s%10])
    else:
        print('zero')
i = int(input('Введите число (1-999): '))
print(f(i))