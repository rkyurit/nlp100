def bigram(sentence):
    chars = list(sentence.replace(' ', ''))

    return [chars[i] + chars[i+1] for i in range(len(chars)) if i + 1 < len(chars)]


str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(bigram(str1))
Y = set(bigram(str2))
print('X : ')
print(X)
print('Y : ')
print(Y)
print('和集合')
# print(list(set(X+Y)))
print(X | Y)
print('積集合')
print(X & Y)
print('差集合')
print(X-Y)
