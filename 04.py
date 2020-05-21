str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# tupleをそのままdictに渡せる
print(dict([(s[0], i) if i in one else (s[:2], i) for i, s in enumerate(str.split(' '), 1)]))
