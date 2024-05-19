import pickle


class A:
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f"A({self.a})"


class B:
    def __init__(self):
        self.b = [A({1, 2, 3}), A([5, 6, 7]), A((True, False, None))]

    def __repr__(self):
        return f"B({self.b})"


byte = pickle.dumps(B())
object_ = pickle.loads(byte)
print(isinstance(byte, bytes))
print(isinstance(object_, B))
print(object_)