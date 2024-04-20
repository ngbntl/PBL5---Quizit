def func(a, b, c):
    print(a,b,c)

d = {'a': 3, 'b': True, 'c': {'d': 'hello', 'e': 5}}
func(**d)