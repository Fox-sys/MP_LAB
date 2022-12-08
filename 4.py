def digital_root(n):
    # Не совсем понятно что это должно быть, но если это корень десятой степени то просто return n**0.1
    return n if n < 10 else digital_root(sum(map(int, str(n))))


print(digital_root(123456789))