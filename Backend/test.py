# import json
#
#
# class B:
#     def __init__(self, data: dict):
#         self.data = data
#
#     def to_dict(self):
#         return self.data
#
#     @staticmethod
#     def from_dict(d):
#         return B(d)
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#
# class C:
#     def __init__(self, data: dict):
#         self.data = data
#
#     def to_dict(self):
#         return self.data
#
#     @staticmethod
#     def from_dict(d):
#         return C(d)
#
#     def __repr__(self):
#         return str(self.data)
#
#
# class CEncoder(json.JSONEncoder):
#     def default(self, obj):
#         return obj.to_dict()
#
#
# # Create an object of class C
# c = C({'a': B({'x': 100, 'y': False, 'z': None}), 'b': None})
#
# # Use json.dumps() to convert the object to a JSON string
# s = json.dumps(c, cls=CEncoder)
# print(s)
#
# # Use json.loads() to convert the JSON string back to an object
# c2 = json.loads(s, object_hook=C.from_dict)
# # c3 = json.loads(c2.to_dict()['a'], object_hook=B.from_dict)
# c3 = c2.to_dict()['a']
# print(c2.to_dict())
# print(c2.__dict__)
import json

# class Answer:
#     def __init__(self, data: dict) -> None:
#         self.id: str | None = data.get("id")
#         self.content: str | None = data.get("content")
#         self.is_correct: bool | None = data.get("is_correct")
#
#     @staticmethod
#     def from_dict(data: dict):
#         return Answer(data)
#
#     def __iter__(self):
#         for key, value in self.__dict__.items():
#             yield key, value
#         # yield 'id', self.id
#         # yield 'content', self.content
#         # yield 'is_correct', self.is_correct
#
# a = Answer({'content': 'abc', 'is_correct': True})
# print(a.__dict__)
# print(dict(a))

import pickle

# Assuming data is your list of dictionaries
binary_data = pickle.dumps([
    {'id': 1, 'a': True, 'b': None},
    {'id': 2, 'a': False, 'b': 5.5}
])
print(type(binary_data))
print(binary_data)

data = pickle.loads(binary_data)
print(type(data))
print(data)