a = input('First: ')
b = input('Second: ')
c = input('Third: ')
if a == b and b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
elif a != b and a != c and b != c:
    print(0)
else:
    print('Условия не выполнены') # Здесь необязательно (всегда будет выполнено одно из условий)
