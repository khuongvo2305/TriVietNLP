# -*- coding: utf-8 -*-

from collections import Counter 

d = [[{}, {'tùng': 1, 'sơn': 1}, {'photo': 1, 'trang_lou': 10, 'quỳnhdinô': 10}], [{}, {'tùng': 1, 'sơn': 1}, {'mơ_ước': 1, 'ảnh': 1, 'trang_lou': 1, 'hp': 1}]]


def flatten(d):
  d0 = Counter()
  d1 = Counter()
  d2 = Counter()

  for doc in d:
    d0 = d0 + Counter(doc[0])
    d1 = d1 + Counter(doc[1])
    d2 = d2 + Counter(doc[2])
  return [dict(d0),dict(d1),dict(d2)]
print(flatten(d))