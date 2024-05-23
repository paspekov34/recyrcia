def test(*args, **kwargs):
    print(args, kwargs)


test(1, 'txt', 3.5, )
test(key1=62, key2=87)

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(7))