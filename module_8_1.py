def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        result = ''
        for i in (a, b):
            if not isinstance(i, str):
                i = str(i)
            result += i
    else:
        if isinstance(result, float):
            result = round(result, 3)
    finally:
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('часть', 'строки'))
